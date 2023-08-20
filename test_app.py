import unittest
from flask import Flask, session
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Convert Amount', response.data)

    def test_result_page_with_valid_data(self):
        data = {
            'Convertfrom': 'USD',
            'Convertto': 'EUR',
            'Convertamount': '100'
        }
        response = self.app.post('/result', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Result', response.data)
        self.assertIn(b'Conversion Result:', response.data)

    def test_result_page_with_invalid_data(self):
        data = {
            'Convertfrom': 'INVALID',
            'Convertto': 'EUR',
            'Convertamount': '100'
        }
        response = self.app.post('/result', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid currency code', response.data)

    def test_is_value_in_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(is_value_in_array(arr, 3))
        self.assertFalse(is_value_in_array(arr, 6))


if __name__ == '__main__':
    unittest.main()
