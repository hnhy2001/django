from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .models import Customer,Oder
from .serializer import CustomerSerializer,OderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OderViewSet(viewsets.ModelViewSet):
    queryset = Oder.objects.all()
    serializer_class = OderSerializer

    
    

def index(request):
    return HttpResponse("hello")

# Create your views here.

class TestView(View):
    def get(self, request):
        return HttpResponse("haha test")
    
