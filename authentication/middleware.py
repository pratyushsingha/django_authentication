from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.contrib import messages
from authentication.validator import validate_turnstile

class TurnstileSocialAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/accounts/social/') and request.method == 'POST':
            token = request.POST.get('cf-turnstile-response')
            if not token:
                messages.error(request, 'Please complete the Turnstile verification')
                return redirect('login')
            
            try:
               validate_turnstile(token)
            except ValidationError:
                messages.error(request, 'Turnstile verification failed')
                return redirect('login')

        response = self.get_response(request)
        return response 