from django.db import models
from users.models import Korisnik
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.
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

    def __repr__(self):
        return f"Knjiga({self.naslov}, {self.isbn}, {self.autor}, {self.zanr}, {self.opis}, {self.godina_izdanja}, {self.korisnik})"

    def __str__(self):
        return self.naslov
    
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