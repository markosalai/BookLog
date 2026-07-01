import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login as django_login
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Korisnik


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    data = json.loads(request.body)

    if Korisnik.objects.filter(email=data.get('email')).exists():
        return JsonResponse({'error': 'Email već postoji'}, status=400)

    try:
        user = Korisnik.objects.create_user(
            email=data['email'],
            ime=data['ime'],
            password=data['password'],
        )
        tokens = get_tokens_for_user(user)
        return JsonResponse({
            'message': 'Registracija uspješna',
            'user': {
                'id': user.id,
                'ime': user.ime,
                'email': user.email,
                'uloga': user.uloga,
            },
            **tokens
        }, status=201)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    data = json.loads(request.body)

    user = authenticate(
        request,
        username=data.get('email'),
        password=data.get('password')
    )

    if user is None:
        return JsonResponse({'error': 'Pogrešan email ili lozinka'}, status=401)

    django_login(request, user)

    tokens = get_tokens_for_user(user)
    return JsonResponse({
        'message': 'Prijava uspješna',
        'user': {
            'id': user.id,
            'ime': user.ime,
            'email': user.email,
            'uloga': user.uloga,
        },
        **tokens
    })