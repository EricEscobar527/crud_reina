"""
URL configuration for crud_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from aplicacion_crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('cerrar/sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar/sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('citas/', views.citas, name='citas'),
    path('citas/canceladas/', views.citas_canceladas, name='citas_canceladas'),
    path('cita/<int:id>', views.cita, name='cita'),
    path('editar/cita/<int:id>', views.editar_cita, name='editar_cita'),
    path('eliminar/cita/<int:id>', views.eliminar_cita, name='eliminar_cita'),
    path('activar/cita/<int:id>', views.activar_cita, name='activar_cita'),
    path('crear/cita/', views.crear_cita, name='crear_cita'),
]
