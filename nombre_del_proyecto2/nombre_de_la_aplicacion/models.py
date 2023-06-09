from django.db import models

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    idtipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    documento = models.CharField(max_length=100)
    lugarresidencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechanacimiento = models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)