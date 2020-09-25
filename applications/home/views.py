from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView

from .models import Prueba
from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resumen.html'

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0','1', '20']

class ListarPrueba(ListView):
    template_name = "home/lista_de_pruebas.html"
    context_object_name = 'pruebas'
    model = Prueba

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/home'

