from django import forms
from .models import Knjiga

class KnjigaForm(forms.ModelForm):
    class Meta:
        model = Knjiga
        fields = ['naslov', 'autor', 'isbn', 'zanr', 'opis', 'godina_izdanja']