from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.


class cartTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret321'}
        User.objects.create_user(**self.credentials)
         
        
    def test_cart(self):
        response = self.client.post('/user/login/', **self.credentials, follow=True)  
        response = self.client.get('/cart/')
        self.assertEquals(response.status_code, 302)
        #self.assertTemplateUsed(response,"/cart/index.html")
