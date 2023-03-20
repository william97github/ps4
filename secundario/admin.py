from django.contrib import admin
from .models import cliente, juego, alquiler

# Register your models here.
admin.site.register(cliente)
admin.site.register(juego)
admin.site.register(alquiler)
