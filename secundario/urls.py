from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),

    path('listar/cliente/', views.listar_cliente, name='listar_cliente'),
    path('crear/cliente/', views.crear_cliente, name='crear_cliente'),
    path('editar/cliente/<int:cliente_id>', views.editar_cliente, name='editar_cliente'),
    path('eliminar/cliente/<int:cliente_id>', views.eliminar_cliente, name='eliminar_cliente'),

    path('listar/juego/', views.listar_juego, name='listar_juego'),
    path('crear/juego/', views.crear_juego, name='crear_juego'),
    path('editar/juego/<int:juego_id>', views.editar_juego, name='editar_juego'),
    path('eliminar/juego/<int:juego_id>', views.eliminar_juego, name='eliminar_juego'),

    path('listar/alquiler/', views.listar_alquiler, name='listar_alquiler'),
    path('crear/alquiler/', views.crear_alquiler, name='crear_alquiler'),
    path('editar/alquiler/<int:alquiler_id>', views.editar_alquiler, name='editar_alquiler'),
    path('eliminar/alquiler/<int:alquiler_id>', views.eliminar_alquiler, name='eliminar_alquiler')
]