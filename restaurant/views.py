from django.shortcuts import render
from rest_framework import generics

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


def index(request):
	return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	