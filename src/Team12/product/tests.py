from django.test import TestCase
from .models import MealPlan 

# Create your tests here.

class test_Product(TestCase):
    def setUp(self):
        self.qs = MealPlan.objects.all()
        self.data = MealPlan.objects.all()
        mealpackage = MealPlan(1, "testpack", 2000, "something", "non toxic", "https://image.shutterstock.com/image-photo/white-transparent-leaf-on-mirror-260nw-577160911.jpg")
        mealpackage.save()
        self.context = {"products": self.data}

    def test_index(self):
        response = self.client.get('/products/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"products/index.html")

    def test_detailed_product(self):
        response = self.client.get('/products/mealplan/1/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"products/mealplan_detailed.html")

    def test_product_order(self):
        response = self.client.get('/products/product_order/price/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"products/index.html")
    
    def test_filter_price(self):
        response = self.client.get('/products/filter_price/10/110/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,"products/index.html")