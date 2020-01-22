# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

from .models import Eventos

#tomado de https://blog.nubecolectiva.com/como-crear-un-crud-con-django-2-y-bootstrap-4-parte-2-python-3-7/
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms


#Listar Eventos
class EventosListado(ListView): 
    model = Eventos # Llamamos a la clase 'Eventos' que se encuentra en nuestro archivo 'models.py'

#Crear Eventos

class EventoCrear(SuccessMessageMixin, CreateView): 
    model = Eventos # Llamamos a la clase 'Eventos' que se encuentra en nuestro archivo 'models.py'
    form = Eventos # Definimos nuestro formulario con el nombre de la clase o modelo 'Eventos'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Eventos' de nuestra Base de Datos 
    success_message = 'Evento Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Eventos
    # Redireccionamos a la página principal luego de crear un registro o evento
    def get_success_url(self): 
        print("hola")       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

#Leer eventos
class EventoDetalle(DetailView): 
    model = Eventos # Llamamos a la clase 'Eventos' que se encuentra en nuestro archivo 'models.py'

#Actualizar (Update) Eventos
class EventoActualizar(SuccessMessageMixin, UpdateView): 
    model = Eventos # Llamamos a la clase 'Eventos' que se encuentra en nuestro archivo 'models.py' 
    form = Eventos # Definimos nuestro formulario con el nombre de la clase o modelo 'Eventos' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Eventos' de nuestra Base de Datos 
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Eventos
    # Redireccionamos a la página principal luego de actualizar un registro o Eventos
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


#Eliminar (Delete) Eventos
class EventoEliminar(SuccessMessageMixin, DeleteView): 
    model = Eventos 
    form = Eventos
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Evento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Evento
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
