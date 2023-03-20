from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.nombre
class juego(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.titulo
class alquiler(models.Model):
    consolas = (('Primero', 'Primero'), ('Segundo', 'Segundo'), ('Tercero', 'Tercero'), ('Cuarto', 'Cuarto'), ('Quinto', 'Quinto'))
    mandos = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'))
    hora_entrada = models.DateTimeField(null=False)
    hora_salida = models.DateTimeField(null=False)
    consola = models.CharField(choices=consolas, null= False, max_length= 10)
    mando = models.CharField(choices=mandos, null= False, max_length= 1)
    clientes = models.ForeignKey(cliente, on_delete=models.CASCADE)
    juegos = models.ForeignKey(juego, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    adicional = models.BooleanField(default=False)




