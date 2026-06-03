from django.contrib import admin

from .models import Knjiga, Recenzija

# Register your models here.
admin.site.register(Knjiga)
admin.site.register(Recenzija)