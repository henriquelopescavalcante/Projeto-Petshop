from django.contrib import admin
from reserva.models import Reserva, Petshop

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'email', 'nome_pet']
    list_display = ['nome', 'data', 'finalizado', 'turno', 'tamanho']


admin.site.register([Petshop])
