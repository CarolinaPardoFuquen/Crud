# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class Eventos(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    Conferencia= 'Conferencia'
    Seminario= 'Seminario'
    Congreso= 'Congreso'
    Curso= 'Curso'
    categorias = [
        (Conferencia, 'Conferencia'),
        (Seminario, 'Seminario'),
        (Congreso, 'Congreso'),
        (Curso, 'Curso'),
    ]
    categoria = models.CharField(
        max_length=22,
        choices=categorias,
        default=Curso,
    )
    # def is__upperclass(self):
    # 	return self.categoriass in {self.Conferencia, self.Curso}
    	
    lugar = models.CharField(max_length=20, default='DEFAULT VALUE')
    direccion = models.CharField(max_length=20, default='DEFAULT VALUE')
    fechainicio = models.CharField(max_length=20, default='DEFAULT VALUE') #models.DateTimeField(null=True, blank=True)
    fechafin= models.CharField(max_length=20, default='DEFAULT VALUE') #models.DateTimeField(null=True, blank=True)
    Presencial = 'Presencial '
    Virtual= 'Virtual'
    tipo_eventos =[
        (Presencial, 'Presencial'),
        (Virtual, 'Virtual'),
    ]
    tipo_evento = models.CharField(
        max_length=22,
        choices=tipo_eventos,
        default=Presencial,
    )

    # class tipo_evento(models.TextChoices):
    #Presencial=1
    #Virtual=2

    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    class Meta:
    	db_table = 'eventos'