import datetime as dt

from django.core.management.base import BaseCommand
from reserva.models import Reserva

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        hoje = dt.date.today()
        data_limite = hoje - dt.timedelta(days=3)
        reservas = Reserva.objects.filter(data__lte=data_limite)
        reservas.update(finalizado=True)
