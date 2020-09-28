from django.test import TestCase, SimpleTestCase, Client

from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm 
from user import views

# Create your tests here.

import sys



class FrontPageTest(TestCase):
    
    
    #DATABASES = 'default'
    #Experimental test
    def test_homepage(self): #This should return as false until we have a homepage
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("user_page.html")

    def test_product_site(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 301)
        response = self.client.get('/cart')
        self.assertEqual(response.status_code, 301)

    def test_register(self):
        form = UserCreationForm()
        self.assertIsNotNone(form)
    
    #def test_login_and_logout(self):
        #response = self.client.get('/user/')
        # asserts if the get is successful
        #self.assertEquals(response.status_code, 200)
        #self.assertTrue("Login" in str(response.content))

        # logs in a dummy user
        #response = self.client.login(username='admin', password='admin')
        #response = self.client.get('/profile/')
        #self.assertEquals(response.status_code, 200)
        #print(response.content)
        # asserts if Logout is available
        #self.assertTrue('Logout' in str(response.content))
