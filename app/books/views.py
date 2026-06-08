import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.models import Avg
from .models import Knjiga, Recenzija

# GET /api/books
@require_http_methods(["GET"])
def book_list(request):
    books = Knjiga.objects.annotate(
        prosjecna_ocjena=Avg('recenzija__ocjena')
    ).values(
        'id', 'naslov', 'autor', 'isbn',
        'zanr', 'godina_izdanja', 'prosjecna_ocjena'
    )
    return JsonResponse({'books': list(books)})


# GET/POST /api/books
@csrf_exempt
@require_http_methods(["POST"])
def book_create(request):
    data = json.loads(request.body)
    try:
        knjiga = Knjiga.objects.create(
            naslov=data['naslov'],
            autor=data['autor'],
            isbn=data['isbn'],
            zanr=data.get('zanr', ''),
            opis=data.get('opis', ''),
            godina_izdanja=data.get('godina_izdanja'),
            korisnik=request.user
        )
        return JsonResponse({
            'id': knjiga.id,
            'naslov': knjiga.naslov,
            'autor': knjiga.autor,
            'isbn': knjiga.isbn,
        }, status=201)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)


# GET /api/books/{id}
@require_http_methods(["GET"])
def book_detail(request, id):
    try:
        knjiga = Knjiga.objects.get(id=id)
    except Knjiga.DoesNotExist:
        return JsonResponse({'error': 'Knjiga nije pronađena'}, status=404)

    recenzije = Recenzija.objects.filter(knjiga_id=id).values(
        'id', 'tekst', 'ocjena', 'vidljiva',
        'datum_pisanja', 'korisnik__ime'
    )
    return JsonResponse({
        'id': knjiga.id,
        'naslov': knjiga.naslov,
        'autor': knjiga.autor,
        'isbn': knjiga.isbn,
        'zanr': knjiga.zanr,
        'opis': knjiga.opis,
        'godina_izdanja': knjiga.godina_izdanja,
        'recenzije': list(recenzije)
    })


# PUT /api/books/{id}
@csrf_exempt
@require_http_methods(["PUT"])
def book_update(request, id):
    try:
        knjiga = Knjiga.objects.get(id=id)
    except Knjiga.DoesNotExist:
        return JsonResponse({'error': 'Knjiga nije pronađena'}, status=404)

    data = json.loads(request.body)

    allowed = ['naslov', 'autor', 'isbn', 'zanr', 'opis', 'godina_izdanja']
    filtered = {k: v for k, v in data.items() if k in allowed}
    
    knjiga.update(**filtered)
    return JsonResponse({
        'id': knjiga.id,
        'naslov': knjiga.naslov,
        'autor': knjiga.autor,
        'isbn': knjiga.isbn,
    })


# DELETE /api/books/{id}
@csrf_exempt
@require_http_methods(["DELETE"])
def book_delete(request, id):
    try:
        knjiga = Knjiga.objects.get(id=id)
    except Knjiga.DoesNotExist:
        return JsonResponse({'error': 'Knjiga nije pronađena'}, status=404)

    knjiga.delete()
    return JsonResponse({'message': 'Knjiga obrisana'}, status=200)


# POST /api/books/{id}/reviews
@csrf_exempt
@require_http_methods(["POST"])
def book_reviews(request, id):
    try:
        knjiga = Knjiga.objects.get(id=id)
    except Knjiga.DoesNotExist:
        return JsonResponse({'error': 'Knjiga nije pronađena'}, status=404)

    data = json.loads(request.body)
    try:
        recenzija = Recenzija.create(
            tekst=data.get('tekst', ''),
            ocjena=data['ocjena'],
            korisnik=request.user,
            knjiga=knjiga
        )
        return JsonResponse({
            'id': recenzija.id,
            'tekst': recenzija.tekst,
            'ocjena': recenzija.ocjena,
        }, status=201)
    except KeyError as e:
        return JsonResponse({'error': f'Missing field: {e}'}, status=400)


# DELETE /api/reviews/{id}
@csrf_exempt
@require_http_methods(["DELETE"])
def review_delete(request, id):
    try:
        recenzija = Recenzija.objects.get(id=id)
    except Recenzija.DoesNotExist:
        return JsonResponse({'error': 'Recenzija nije pronađena'}, status=404)

    recenzija.delete()
    return JsonResponse({'message': 'Recenzija obrisana'}, status=200)