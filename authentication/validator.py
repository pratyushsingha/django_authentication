import requests
from django.core.exceptions import ValidationError
from django.conf import settings

def validate_turnstile(token):
    """
    Validates the Turnstile token by sending a request to Cloudflare's Turnstile API.
    """
    turnstile_secret_key = settings.TURNSTILE_SECRET_KEY
    if not turnstile_secret_key:
        raise ValidationError("Turnstile secret key not configured.")
    
    response = requests.post(
        'https://challenges.cloudflare.com/turnstile/v0/siteverify',
        data={
            'secret': turnstile_secret_key,
            'response': token,
        }
    )

    result = response.json()
    if not result.get('success'):
        raise ValidationError("Turnstile verification failed.")
