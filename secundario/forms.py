from django import forms
from .models import cliente, juego, alquiler

from datetime import datetime, timedelta

ahora = datetime.now()
despues = ahora + timedelta(minutes=30)

class clienteform(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class juegoform(forms.ModelForm):
    class Meta:
        model = juego
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'})
        }

class alquilerform(forms.ModelForm):
    class Meta:
        model = alquiler
        fields = ['hora_entrada', 'hora_salida', 'consola', 'mando', 'clientes', 'juegos', 'estado', 'adicional']
        widgets = {
            'hora_entrada': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime', 'value': ahora.strftime("%d/%m/%Y %H:%M")}),
            'hora_salida': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime', 'value': despues.strftime("%d/%m/%Y %H:%M")}),
            'consola': forms.Select(attrs={'class': 'form-control'}),
            'mando': forms.Select(attrs={'class': 'form-control'}),
            'clientes': forms.Select(attrs={'class': 'form-control'}),
            'juegos': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'adicional': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }