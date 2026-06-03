from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class KorisnikManager(BaseUserManager):
    def create_user(self, email, ime, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, ime=ime, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, ime, password=None, **extra_fields):
        extra_fields.setdefault('uloga', Korisnik.Uloga.ADMIN)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, ime, password, **extra_fields)

# Create your models here.
class Korisnik(AbstractBaseUser, PermissionsMixin):
    class Uloga(models.TextChoices):
        ADMIN = "admin"
        USER = "user"

    ime = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    datum_registracije = models.DateField(auto_now_add=True)
    uloga = models.CharField(
        max_length=10,
        choices=Uloga.choices,
        default=Uloga.USER
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = KorisnikManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["ime"]

    def __str__(self):
        return self.email
