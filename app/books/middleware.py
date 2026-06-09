from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from users.models import Korisnik


def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Token nije pronađen'}, status=401)

        token_str = auth_header.split(' ')[1]

        try:
            token = AccessToken(token_str)
            user_id = token['user_id']
            request.user = Korisnik.objects.get(id=user_id)
        except (TokenError, InvalidToken):
            return JsonResponse({'error': 'Token nije validan'}, status=401)
        except Korisnik.DoesNotExist:
            return JsonResponse({'error': 'Korisnik nije pronađen'}, status=401)

        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'Token nije pronađen'}, status=401)

        token_str = auth_header.split(' ')[1]

        try:
            token = AccessToken(token_str)
            user_id = token['user_id']
            request.user = Korisnik.objects.get(id=user_id)
        except (TokenError, InvalidToken):
            return JsonResponse({'error': 'Token nije validan'}, status=401)
        except Korisnik.DoesNotExist:
            return JsonResponse({'error': 'Korisnik nije pronađen'}, status=401)

        if request.user.uloga != 'admin':
            return JsonResponse({'error': 'Nemate ovlasti'}, status=403)

        return view_func(request, *args, **kwargs)
    return wrapper