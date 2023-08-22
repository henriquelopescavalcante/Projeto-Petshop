from model_bakery import baker
from reserva.models import Reserva


total = 50

print('Criando agendamentos')
for i in range(total):
    reserva = baker.make(Reserva)
    reserva.save()

print(f'{total} agendamentos criados!!')
