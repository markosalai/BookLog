from django.db import models
from users.models import Korisnik
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.

class KnjigaManager(models.Manager):
    def find_all(self):
        return self.all()

    def find_by_user(self, korisnik_id):
        return self.filter(korisnik_id=korisnik_id)

    def find_by_id(self, id):
        return self.filter(id=id).first()
    
    def search(self, query):
        return self.filter(
            models.Q(naslov__icontains=query) |
            models.Q(autor__icontains=query) |
            models.Q(zanr__icontains=query)
        )


class Knjiga(models.Model):
    naslov = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=17, unique=True)
    zanr = models.CharField(max_length=255, blank=True, null=True)
    opis = models.TextField(blank=True, null=True)
    godina_izdanja = models.PositiveSmallIntegerField()

    korisnik = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    objects = KnjigaManager()

    def __repr__(self):
        return f"Knjiga({self.naslov}, {self.isbn}, {self.autor}, {self.zanr}, {self.opis}, {self.godina_izdanja}, {self.korisnik})"

    def __str__(self):
        return f"{self.naslov} - {self.autor}"
    
    @classmethod
    def create(cls, naslov, autor, isbn, korisnik, **kwargs):
        return cls.objects.create(
            naslov=naslov,
            autor=autor,
            isbn=isbn,
            korisnik=korisnik,
            **kwargs
        )
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self

    def delete_knjiga(self):
        self.delete()


class RecenzijaManager(models.Manager):
    def find_by_book(self, knjiga_id):
        return self.filter(knjiga_id=knjiga_id)

    def find_by_user(self, korisnik_id):
        return self.filter(korisnik_id=korisnik_id)
    
class Recenzija(models.Model):
    tekst = models.TextField(blank=True, null=True)
    vidljiva = models.BooleanField(default=True)
    datum_pisanja = models.DateField(auto_now_add=True)
    ocjena = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    korisnik = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    knjiga = models.ForeignKey(Knjiga, on_delete=models.CASCADE)

    objects = RecenzijaManager()

    @classmethod
    def create(cls, tekst, ocjena, korisnik, knjiga):
        return cls.objects.create(
            tekst=tekst,
            ocjena=ocjena,
            korisnik=korisnik,
            knjiga=knjiga,
        )
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        return self
    
    def toggle_visibility(self):
        self.vidljiva = not self.vidljiva
        self.save()

    class Meta:
        unique_together = [('korisnik', 'knjiga')]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(ocjena__gte=1) & models.Q(ocjena__lte=5),
                name="ocjena_between_1_and_5"
            )
        ]
        
    def __str__(self):
        return "Recenzija"