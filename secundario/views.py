from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import clienteform, juegoform, alquilerform
from .models import cliente, juego, alquiler

from django.db.models import Count

from datetime import datetime, timedelta

ahora = datetime.now().isoweekday()
hoy = datetime.now()
if ahora == 1:
    nuevo = datetime(hoy.year, hoy.month, hoy.day, 00, 00, 00, 00000)
    inicio = (nuevo - timedelta(days=0)).strftime("%Y-%m-%d %H:%M")
    fin = (nuevo + timedelta(days=7)).strftime("%Y-%m-%d %H:%M")
elif ahora == 2:
    nuevo = datetime(hoy.year, hoy.month, hoy.day, 00, 00, 00, 00000)
    inicio = (nuevo - timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
    fin = (nuevo + timedelta(days=6)).strftime("%Y-%m-%d %H:%M")
elif ahora == 3:
    nuevo = datetime(hoy.year, hoy.month, hoy.day, 00, 00, 00, 00000)
    inicio = (nuevo - timedelta(days=2)).strftime("%Y-%m-%d %H:%M")
    fin = (nuevo + timedelta(days=5)).strftime("%Y-%m-%d %H:%M")
elif ahora == 4:
    nuevo = datetime(hoy.year, hoy.month, hoy.day, 00, 00, 00, 00000)
    inicio = (nuevo - timedelta(days=3)).strftime("%Y-%m-%d %H:%M")
    fin = (nuevo + timedelta(days=4)).strftime("%Y-%m-%d %H:%M")
elif ahora == 5:
    nuevo = datetime(hoy.year, hoy.month, hoy.day, 00, 00, 00, 00000)
    inicio = (nuevo - timedelta(days=4)).strftime("%Y-%m-%d %H:%M")
    fin = (nuevo + timedelta(days=3)).strftime("%Y-%m-%d %H:%M")
elif ahora == 6:
    nuevo = datetime(hoy.year, hoy.month, hoy.day, 00, 00, 00, 00000)
    inicio = (nuevo - timedelta(days=5)).strftime("%Y-%m-%d %H:%M")
    fin = (nuevo + timedelta(days=2)).strftime("%Y-%m-%d %H:%M")
elif ahora == 7:
    nuevo = datetime(hoy.year, hoy.month, hoy.day, 00, 00, 00, 00000)
    inicio = (nuevo - timedelta(days=6)).strftime("%Y-%m-%d %H:%M")
    fin = (nuevo + timedelta(days=1)).strftime("%Y-%m-%d %H:%M")


# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('dashboard')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'el usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'no coincide las contraseñas'
        })

def signout(request):
    logout(request)
    return redirect('dashboard')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'usuario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect('dashboard')

def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html', {
            'lists': alquiler.objects.filter(estado = False),
            'lists1': alquiler.objects.filter(hora_entrada__range=(inicio, fin), estado = True, adicional = False),
            'count1': cliente.objects.all().count(),
            'count2': juego.objects.all().count()
        })

def listar_cliente(request):
    if request.method == 'GET':
        return render(request, 'listar_cliente.html', {
            'lists': cliente.objects.all()
        })

@login_required
def crear_cliente(request):
    if request.method == 'GET':
        return render(request, 'crear_cliente.html', {
            'form': clienteform,
        })
    else:
        try:
            form = clienteform(request.POST)
            form.save()
            return redirect('listar_cliente')
        except:
            return render(request, 'crear_cliente.html', {
                'form': clienteform,
                'error': 'Ingrese datos validos'
            })

@login_required
def editar_cliente(request, cliente_id):
    if request.method == 'GET':
        detalle = get_object_or_404(cliente, pk=cliente_id)
        form = clienteform(instance=detalle)
        return render(request, 'editar_cliente.html', {
            'form': form
        })
    else:
        try:
            detalle = get_object_or_404(cliente, pk=cliente_id)
            form = clienteform(request.POST, instance=detalle)
            form.save()
            return redirect('listar_cliente')
        except:
            return render(request, 'editar_cliente.html', {
                'form': form,
                'error': 'fallo en actualizar'
            })

@login_required
def eliminar_cliente(request, cliente_id):
    if request.method == 'GET':
        detalle = get_object_or_404(cliente, pk=cliente_id)
        detalle.delete()
        return redirect('listar_cliente')


def listar_juego(request):
    if request.method == 'GET':
        return render(request, 'listar_juego.html', {
            'lists': juego.objects.all()
        })

@login_required
def crear_juego(request):
    if request.method == 'GET':
        return render(request, 'crear_juego.html', {
            'form': juegoform,
        })
    else:
        try:
            form = juegoform(request.POST)
            form.save()
            return redirect('listar_juego')
        except:
            return render(request, 'crear_juego.html', {
                'form': juegoform,
                'error': 'Ingrese datos validos'
            })

@login_required
def editar_juego(request, juego_id):
    if request.method == 'GET':
        detalle = get_object_or_404(juego, pk=juego_id)
        form = juegoform(instance=detalle)
        return render(request, 'editar_juego.html', {
            'form': form
        })
    else:
        try:
            detalle = get_object_or_404(juego, pk=juego_id)
            form = juegoform(request.POST, instance=detalle)
            form.save()
            return redirect('listar_juego')
        except:
            return render(request, 'editar_juego.html', {
                'form': form,
                'error': 'fallo en actualizar'
            })

@login_required
def eliminar_juego(request, juego_id):
    if request.method == 'GET':
        detalle = get_object_or_404(juego, pk=juego_id)
        detalle.delete()
        return redirect('listar_juego')

@login_required
def listar_alquiler(request):
    if request.method == 'GET':
        return render(request, 'listar_alquiler.html', {
            'lists': alquiler.objects.all()
        })

@login_required
def crear_alquiler(request):
    if request.method == 'GET':
        return render(request, 'crear_alquiler.html', {
            'form': alquilerform,
        })
    else:
        try:
            form = alquilerform(request.POST)
            form.save()
            return redirect('listar_alquiler')
        except:
            return render(request, 'crear_alquiler.html', {
                'form': alquilerform,
                'error': 'Ingrese datos validos'
            })

@login_required
def editar_alquiler(request, alquiler_id):
    if request.method == 'GET':
        detalle = get_object_or_404(alquiler, pk=alquiler_id)
        form = alquilerform(instance=detalle)
        return render(request, 'editar_alquiler.html', {
            'form': form
        })
    else:
        try:
            detalle = get_object_or_404(alquiler, pk=alquiler_id)
            form = alquilerform(request.POST, instance=detalle)
            form.save()
            return redirect('listar_alquiler')
        except:
            return render(request, 'editar_alquiler.html', {
                'form': form,
                'error': 'fallo en actualizar'
            })

@login_required
def eliminar_alquiler(request, alquiler_id):
    if request.method == 'GET':
        detalle = get_object_or_404(alquiler, pk=alquiler_id)
        detalle.delete()
        return redirect('listar_alquiler')