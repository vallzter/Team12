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
        response = self.client.post('/user/login/', **self.credentials, follow=True)  
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_profile(self):
        response = self.client.post('/user/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/user/register/')
        self.assertEqual(response.status_code, 200)
        


    def test_editprofile(self):
        response = self.client.post('/user/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/user/editProfile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("user/edit.html")
        response = self.client.get('/user/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("user/edit.html")

    def test_register(self):
        response = self.client.get('/user/register/')
        self.assertTemplateUsed(response, "user/register.html")

class removeUser(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser2',
            'password': 'secret3211231'}
        self.supercredentials = {
            'username': 'administrator',
            'password': 'GobleGobleTwinkleGobble123'} 
        User.objects.create_superuser(**self.supercredentials)
        response = self.client.post('/admin/', **self.supercredentials)  



    def test_remove_user(self):
        response = self.client.post('/user/login/', **self.supercredentials, follow=True)
        response = self.client.post('/user/remove/') 
        self.assertEqual(response.status_code, 200)
        responseExtra = self.client.post('/user/admin/', **self.credentials, follow=True)
        responseExtra = self.client.post('/user/remove/') 
        self.assertEqual(responseExtra.status_code, 200)

