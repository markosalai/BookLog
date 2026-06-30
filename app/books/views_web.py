from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import KnjigaForm

# these views just serve the templates
# actual data is loaded via Fetch API calls to /api/ endpoints

@ensure_csrf_cookie
def knjizna_polica(request):
    return render(request, 'books/knjizna_polica.html')

@ensure_csrf_cookie
def knjiga_detalji(request, id):
    return render(request, 'books/knjiga_detalji.html', {'knjiga_id': id})

@ensure_csrf_cookie
def knjiga_dodaj(request):
    if request.method == 'POST':
        form = KnjigaForm(request.POST)
        if form.is_valid():
            knjiga = form.save(commit=False)
            knjiga.korisnik = request.user
            knjiga.save()
            return redirect('knjizna_polica')
    else:
        form = KnjigaForm()
    return render(request, 'books/knjiga_form.html', {'form': form})