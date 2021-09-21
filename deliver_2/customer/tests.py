from django.test import TestCase

class URLTests(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_testorder(self):
        response = self.client.get('/order/')
        self.assertEqual(response.status_code, 200)
    def test_testorder(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_testorder(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
    
    def test_testerror(self):
        response = self.client.get('/error')
        self.assertEqual(response.status_code, 200)
    
