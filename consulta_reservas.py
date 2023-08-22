import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'ultima.settings'

django.setup()

from reserva.models import Reserva

print(Reserva.objects.count())
