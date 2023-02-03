from rest_framework.serializers import ModelSerializer
from .models import Booking, Menu


class MenuSerializer(ModelSerializer):
	class Meta:
		model = Menu
		fields = ['title', 'price', 'inventory']

class BookingSerializer(ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'
		