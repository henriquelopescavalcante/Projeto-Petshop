from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reserva.models import Petshop, Reserva
from rest_api.serializers import AgendamentoModelSerializer, PetshopModelSerializer

# Create your views here.

class AgendamentoModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = AgendamentoModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PetshopModelViewSet(ModelViewSet):
    queryset = Petshop.objects.all()
    serializer_class = PetshopModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({'message': f'Hello, {request.data.get("name")}'})

    return Response({'hello': 'World API'})
