'''
Implementación de la base de datos donde se lleva el registro del municipio, parroquia, sector y clap
asi como su respectiva cantidad de litros de gas y numero de familias.
'''

from django.db import models

class Municipio(models.Model):
    nombre_mun = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_mun

class Parroquia(models.Model):
    id_municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    nombre_par = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_par

class Sector(models.Model):
    id_parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    nombre_sec = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_sec

class Clap(models.Model):
    id_sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    nombre_clap = models.CharField(max_length=30)
    total_familias = models.IntegerField
    total_litros = models.IntegerField

    def __str__(self):
        return self.nombre_clap

