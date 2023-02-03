from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from restaurant.models import Booking, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer


def index(request):
	return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer
	
class BookingViewSet(ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [permissions.IsAuthenticated]
