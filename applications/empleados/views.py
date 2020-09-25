from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
	template_name = 'inicio.html'


class ListAllEmpleados(ListView):
	template_name = 'empleado/list_all.html'
	paginate_by = 5
	ordering = "first_name"
	context_object_name = 'empleado'

	def get_queryset(self):
		palabra_clave = self.request.GET.get("kword", '')
		lista = Empleado.objects.filter(
			first_name__icontains=palabra_clave
		)
		return lista


class ListaEmpleadosAdmin(ListView):
	template_name = 'empleado/lista_empleados.html'
	paginate_by = 5
	ordering = "first_name"
	context_object_name = 'empleado'
	model = Empleado


class ListByAreaEmpleado(ListView):
	template_name = 'empleado/list_by-areas.html'
	context_object_name = 'empleados'

	def get_queryset(self):
		area = self.kwargs['shortname']
		lista = Empleado.objects.filter(departamento__short_name = area)
		return lista


class ListEmpleadosByKword(ListView):
	template_name = 'empleado/by_kword.html'
	context_object_name = 'empleados'

	def get_queryset(self):
		print('********')
		palabra_clave = self.request.GET.get("kword",)
		print("=====", palabra_clave)
		lista = Empleado.objects.filter(first_name = palabra_clave)
		print("lista resultado: ", lista)
		return lista


class ListHabilidadesEmpleado(ListView):
	template_name = 'empleado/habilidades.html'
	context_object_name = 'habilidades'

	def get_queryset(self):
		empleado = Empleado.objects.get(id=4)
		return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
	model = Empleado
	template_name = 'empleado/detail_empleado.html'

	def get_context_data(self, **kwargs):
		context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
		context['titulo'] = 'Empleado del mes'
		return context

class SuccessView(TemplateView):
	template_name = "empleado/success.html"

class EmpleadoCreateView(CreateView):
	model = Empleado
	template_name = 'empleado/add.html'
	form_class = EmpleadoForm
	success_url = reverse_lazy('persona_app:empleados_admin')

	def form_valid(self, form):
		empleado = form.save(commit=False)
		empleado.full_name = empleado.first_name + ' ' + empleado.last_name
		empleado.save()
		return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
	model = Empleado
	template_name = 'empleado/update.html'
	fields = [
		'first_name',
		'last_name',
		'job',
		'departamento',
		'habilidades'
	]
	success_url = reverse_lazy('persona_app:empleados_admin')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		print('*******METODO POST*************')
		print('==========')
		print(request.POST)
		print(request.POST['last_name'])
		return super().post(request, *args, **kwargs)
	
	def form_valid(self, form):
		print('*******METODO POST*************')
		print('***********')
		return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
	model = Empleado
	template_name = 'empleado/delete.html'
	success_url = reverse_lazy('persona_app:empleados_admin')




