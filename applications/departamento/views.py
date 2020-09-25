from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .forms import NewDepartamentoForm
from applications.empleados.models import Empleado
from .models import Departamento

class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = 'departamentos'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/departamento/new-departamento/'

    def form_valid(self, form):
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name= form.cleaned_data['shortname']
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name= nombre,
            last_name= apellido,
            job='1',
            departamento= depa

        )

        return super(NewDepartamentoView,self).form_valid(form)
