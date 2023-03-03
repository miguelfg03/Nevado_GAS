from django.db import models

# Create your models here.

class Municipio(models.Model):
    nombre_mun = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_mun

class Parroquia(models.Model):
    id_municipio = models.ForeignKey(Municipio)
    nombre_par = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_par

class Sector(models.Model):
    id_parroquia = models.ForeignKey(Parroquia)
    nombre_sec = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_sec

class Clap(models.Model):
    id_sector = models.ForeignKey(Sector)
    nombre_clap = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_clap

