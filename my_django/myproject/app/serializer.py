from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Customer,Oder

class OderSerializer(ModelSerializer):
    class Meta:
        model = Oder
        fields = ['id']

class CustomerSerializer(ModelSerializer):
    oder = OderSerializer()
    class Meta:
        model = Customer
        fields = ['id', 'userName', 'createdDate', 'oder_id']