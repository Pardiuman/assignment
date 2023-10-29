import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    # this is SUCCESS test case
    def test_hello_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    # this is FAILURE test case
    # def test_unexisted_route(self):
    #     response = self.app.get('/route')
    #     self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()