import pytest
import datetime as dt

from model_bakery import baker

from reserva.models import Petshop, Reserva
from rest_api.serializers import AgendamentoModelSerializer


@pytest.fixture
def agendamento():
    return baker.make(Reserva)


@pytest.mark.django_db
def test_agendamento_serializer(agendamento):
    # agendamento = baker.make(Reserva)
    serializer = AgendamentoModelSerializer(instance=agendamento)
    assert serializer.data["nome_pet"] == agendamento.nome_pet
    petshop = baker.make(Petshop)
    dados = {
        "nome": "teste",
        "petshop": petshop.id,
        "nome_pet": "teste pet",
        "email": "email@email.com",
        "data": dt.date.today() - dt.timedelta(days=10),
        "observacoes": "",
        "tamanho": 10,
        "turno": "tarde",
    }
    serializer = AgendamentoModelSerializer(data=dados)
    serializer.is_valid(raise_exception=False)
    assert 'data' in serializer.errors
    assert 'tamanho' in serializer.errors
