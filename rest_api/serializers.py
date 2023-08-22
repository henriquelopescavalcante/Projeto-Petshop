import datetime
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)

from reserva.models import Petshop, Reserva


class ReservaPetshopSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'


class PetshopModelSerializer(ModelSerializer):
   
    class Meta:
        model = Petshop
        fields = '__all__'


class PetShopRelatedFieldCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = PetshopNestedModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):
        return self.serializer(value, context=self.context).data


class PetshopNestedModelSerializer(ModelSerializer):
    class Meta:
        model = Petshop
        fields = '__all__'


class AgendamentoModelSerializer(ModelSerializer):

    def validate_data(self, value):
        hoje = datetime.date.today()
        if value < hoje:
            raise ValidationError('Não é possivel realizar um agendamento para o passado')
        return value

    class Meta:
        model = Reserva
        fields = '__all__'
