from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'short_name',
        'job',
        'full_name'
    )
    def full_name(self, obj):
        
        return obj.first_name.capitalize() + ' ' + obj.last_name.upper()

    def short_name(self, obj):
        
        return obj.departamento.short_name.capitalize()

    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)