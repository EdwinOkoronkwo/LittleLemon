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
    # def setUp(self) -> None:
        
    #     Menu.objects.create(title='Bread', price=4.99, inventory=20)
    #     Menu.objects.create(title='Pan Cake', price=12.99, inventory=50)
        
    # def test_getall(self):    
    #     menu = Menu.objects.all()
    #     serializer = MenuSerializer(menu, many=True)
    #     bread = Menu.objects.get(title="bread")
    #     self.assertEqual(bread.title, serializer.data[1].title)
    #     #bread = Menu.objects.get(title="bread")
      
        

