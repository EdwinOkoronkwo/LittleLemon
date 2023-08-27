from django.test import TestCase, Client
from django.contrib.auth.models import User
from restaurant.models import Menu
from .serializers import MenuSerializer


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)
        
        
# class MenuViewTest(TestCase):
#     def setUp(self) -> None:
        
#         self.bread = Menu.objects.create(title='Bread', price=4.99, inventory=20)
#         self.pancake = Menu.objects.create(title='Pan Cake', price=12.99, inventory=50)
        
#     def test_getall(self):    
#         menu = Menu.objects.all()
#         instances = [
#         {'id': 1, 'title': 'Bread', 'price': 4.99, 'inventory': 20},
#        {'id': 2, 'title': 'Pan Cake', 'price': 12.99, 'inventory': 50},
#     ]
#         serializer = MenuSerializer(menu, many=True)
#         self.assertEqual(serializer, instances)

        

