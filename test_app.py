from unittest import TestCase
from app import app
# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

class AppTestCase(TestCase):

    # This method runs before each test case
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # This method runs after each test case
    def tearDown(self):
        pass

    # Test the home page
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your details:', response.data)

    # Test the result page with valid data
    def test_valid_result_page(self):
        response = self.app.get('/result?Convertfrom=USD&Convertto=EUR&Convertamount=100')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The result is:', response.data)

    # Test the result page with invalid amount
    def test_invalid_amount(self):
        response = self.app.get('/result?Convertfrom=USD&Convertto=EUR&Convertamount=invalid')
        self.assertEqual(response.status_code, 302)  # Should redirect to home page
        self.assertIn(b'Please enter a valid amount', response.data)

    # Test the result page with invalid currency code
    def test_invalid_currency_code(self):
        response = self.app.get('/result?Convertfrom=XYZ&Convertto=EUR&Convertamount=100')
        self.assertEqual(response.status_code, 302)  # Should redirect to home page
        self.assertIn(b'Invalid currency code', response.data)

    # Test the result page with invalid amount and currency code
    def test_invalid_amount_and_currency_code(self):
        response = self.app.get('/result?Convertfrom=XYZ&Convertto=EUR&Convertamount=invalid')
        self.assertEqual(response.status_code, 302)  # Should redirect to home page
        self.assertIn(b'Please enter a valid amount', response.data)
        self.assertIn(b'Invalid currency code', response.data)


    def test_value_in_array(self):
        arr = [1, 2, 3, 4, 5]
        value = 3
        result = is_value_in_array(arr, value)
        self.assertTrue(result)
    
    

if __name__ == '__main__':
    unittest.main()
