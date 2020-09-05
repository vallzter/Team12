from django.test import TestCase, SimpleTestCase, Client
from user import views

# Create your tests here.

class FrontPageTest(TestCase):

    #Experimental test
    def test_code(self): #This should return as false until we have a homepage
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)


    def test_login(self):
        testClient = Client()
        isLogged = testClient.post('/login', {'username': 'John', 'password': 'Hrafnkell'})
        isLogged = testClient.get('/customer/details/')
        print(isLogged.content)
        #self.assertEqual(isLogged.status_code, 200)

    