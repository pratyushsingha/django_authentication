from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                if not sociallogin.is_existing:
                    connected_accounts = user.socialaccount_set.all()
                    providers = [account.provider for account in connected_accounts]
                    
                    if providers:
                        provider_names = ', '.join(providers)
                        messages.error(
                            request,
                            f'This email is already registered using {provider_names}. '
                            'Please use that login method instead.'
                        )
                    else:
                        messages.error(
                            request,
                            'This email is already registered. Please login using your email and password.'
                        )
                    raise ImmediateHttpResponse(redirect('login')) 
            except User.DoesNotExist:
                pass 