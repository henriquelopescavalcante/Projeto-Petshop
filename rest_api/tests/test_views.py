import pytest
import datetime as dt

from django.contrib.auth.models import User

from rest_framework.test import APIClient

from model_bakery import baker
from reserva.models import Petshop, Reserva


@pytest.mark.django_db
def test_petshop_listagem_ok():
    cliente = APIClient()
    resposta = cliente.get("/api/petshop")
    resultados = resposta.data["results"]
    assert len(resultados) == 0
    baker.make(Petshop)
    resposta = cliente.get("/api/petshop")
    resultados = resposta.data["results"]
    assert len(resultados) == 1


@pytest.mark.django_db
def test_agendamento_listagem_ok():
    cliente = APIClient()
    resposta = cliente.get("/api/agendamento")
    resultados = resposta.data["results"]
    assert len(resultados) == 0
    baker.make(Reserva, nome="teste")
    resposta = cliente.get("/api/agendamento")
    resultados = resposta.data["results"]
    reserva = resultados[0]
    assert reserva["nome"] == "teste"


@pytest.mark.django_db
def test_criar_petshop_ok():
    cliente = APIClient()
    dados = {
        "nome": "teste",
        "rua": "teste rua",
        "bairro": "bairro teste",
        "numero": "10",
    }
    resposta = cliente.post("/api/petshop", dados)
    assert resposta.status_code == 401
    usuario = baker.make(User)
    cliente.force_authenticate(user=usuario)
    resposta = cliente.post("/api/petshop", dados)
    assert resposta.status_code == 201


@pytest.mark.django_db
def test_criar_petshop_erro():
    cliente = APIClient()
    dados = {
        "nome": "teste",
        "rua": "teste rua",
        "bairro": "bairro teste",
        "numero": "asdasdasdasdasdasasdas",
    }
    usuario = baker.make(User)
    cliente.force_authenticate(user=usuario)
    resposta = cliente.post("/api/petshop", dados)
    assert resposta.status_code == 400


@pytest.mark.django_db
def test_apagar_petshop_ok():
    cliente = APIClient()
    petshop = baker.make(Petshop)
    usuario = baker.make(User)
    cliente.force_authenticate(user=usuario)
    resposta = cliente.delete(f"/api/petshop/{petshop.id}")
    assert Petshop.objects.count() == 0
