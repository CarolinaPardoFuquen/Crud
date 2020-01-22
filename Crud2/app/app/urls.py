"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from eventos.views import EventosListado, EventoDetalle, EventoCrear, EventoActualizar, EventoEliminar

urlpatterns = [

    path('', EventosListado.as_view(template_name = "eventos/index.html"), name='leer'),
    path('admin/', admin.site.urls),
 
    # La ruta 'leer' en donde listamos todos los registros o eventos de la Base de Datos
    path('eventos/', EventosListado.as_view(template_name = "eventos/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un evento o registro 
    path('eventos/detalle/<int:pk>', EventoDetalle.as_view(template_name = "eventos/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo evento o registro  
    path('eventos/crear', EventoCrear.as_view(template_name = "eventos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un evento o registro de la Base de Datos 
    path('eventos/editar/<int:pk>', EventoActualizar.as_view(template_name = "eventos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un evento o registro de la Base de Datos 
    path('eventos/eliminar/<int:pk>', EventoEliminar.as_view(), name='eliminar'),    
]