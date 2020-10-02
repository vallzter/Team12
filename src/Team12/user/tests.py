from django.test import TestCase, SimpleTestCase, Client
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from user import views, models
from cart import views
# Create your tests here.

import sys



class FrontPageTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret321'}
        User.objects.create_user(**self.credentials)

    def testLogin(self):
        response = self.client.post('/user/login/', **self.credentials)  
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.post('/user/login/', **self.credentials)  
        self.assertEqual(response.status_code, 200)
        response = self.client.get('profile/')
        #self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("profile.html")
        #response = self.client.get('/user/edit/')
      #  self.assertEqual(response.status_code, 200)


class removeUser(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret321'}
        User.objects.create_user(**self.credentials)

    def test_remove_user(self):
        response = self.client.post('/user/login/', **self.credentials)  
        response = self.client.post('/user/remove/')  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"user/user_remove.html")


class RegisterTest(TestCase):
    

    def setUp(self):
        form = UserCreationForm()
        #form.cleaned_data.username = "wolfram"
        #self.assertIsNotNone(form)
        #form.save()
        #username = form.cleaned_data.get('username') 
        #password = form.cleaned_data.get('password1') 
        #first_name = form.cleaned_data.get('firstname') 
        #last_name = form.cleaned_data.get('lastname') 
        #email = form.cleaned_data.get('email')

    def test_register(self):
        pass

    #def test_homepage(self): #This should return as false until we have a homepage
        #response = self.client.get('/')
        #self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed("user_page.html")
        #response = self.client.get('/products')
        #self.assertEqual(response.status_code, 301)
        #self.assertTemplateUsed("profile.html")

    #def test_product_site(self):
        #response = self.client.get('/products')
        #self.assertEqual(response.status_code, 200)
        #response = self.client.get('/cart')
        #self.assertEqual(response.status_code, 301)

    #def test_register(self):
        #form = UserCreationForm()
        #self.assertIsNotNone(form)



        # logs in a dummy user
        
        #print(self.user)

        #print(response.content)
        # asserts if Logout is available
        #self.assertTrue('Logout' in str(response.content))
