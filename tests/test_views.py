from django.test import TestCase

from restaurant import models


class MenuViewTest(TestCase):
	def setUp(self):
		item_1 = models.Menu.objects.create(title='IceCream_1', price=10, inventory=100)
		item_2 = models.Menu.objects.create(title='IceCream_2', price=20, inventory=100)
		item_3 = models.Menu.objects.create(title='IceCream_3', price=30, inventory=100)
	
	def test_get_all(self):
		items = models.Menu.objects.all().order_by('title')
		self.assertEqual(len(items), 3)
		self.assertEqual(str(items[0]), 'IceCream_1: 10.00')
		self.assertEqual(str(items[1]), 'IceCream_2: 20.00')
		self.assertEqual(str(items[2]), 'IceCream_3: 30.00')
