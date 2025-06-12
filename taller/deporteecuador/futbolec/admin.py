from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Equipo, Jugador, Campeonato, CameponatoEquipo
from import_export import resources

# Register your models here.

class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo
        exclude = ('id',)  

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EquipoResource
    list_display = ('nombre', 'siglas', 'user_twitter')
    search_fields = ('nombre', 'user_twitter')

class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador
        exclude = ('id',)

class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JugadorResource
    list_display = ('nombre', 'posicion', 'numero', 'sueldo', 'equipo')
    search_fields = ('nombre', 'equipo__nombre')

class CampeonatoResource(resources.ModelResource):
    class Meta:
        model = Campeonato
        exclude = ('id',)

class CampeonatoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CampeonatoResource
    list_display = ('nom_campeonato', 'nom_auspiciador')
    search_fields = ('nom_campeonato', 'nom_auspiciador')

class CameponatoEquipoResource(resources.ModelResource):
    class Meta:
        model = CameponatoEquipo
        exclude = ('id',)

class CameponatoEquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CameponatoEquipoResource
    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('equipo__nombre', 'campeonato__nom_campeonato')

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CameponatoEquipo, CameponatoEquipoAdmin)
