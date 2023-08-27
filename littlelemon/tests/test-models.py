from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)
        
        

class MenuViewTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream : 80')

    def test_get_all(self):
        Menu.objects.create(title="Salmon", price=80, inventory=100)
        Menu.objects.create(title="Steak", price=40, inventory=50)
        items = Menu.objects.all()
        self.assertEqual(str(items), '<QuerySet [<Menu: Salmon : 100.00>, <Menu: Steak : 50.00>]')