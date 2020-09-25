from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'persona_app'

urlpatterns = [
    path('', views.InicioView.as_view()),
    path('listar-todo-empleados', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar-by-area/<shortname>', views.ListByAreaEmpleado.as_view(),name='empleados_area'),
    path('lista-empleados-admin', views.ListaEmpleadosAdmin.as_view(),name='empleados_admin'),
    path('buscar_empleado', views.ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado', views.ListHabilidadesEmpleado.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add-empleado', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),

    ]
