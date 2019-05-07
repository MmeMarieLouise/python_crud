import unittest
import requests

class ApiTest(unittest.TestCase):

    def test_get_home(self):
        r = requests.get('localhost:5000/')
        code = r.status_code
        self.assertEqual(code, 200)


if __name__ == '__main__':
    unittest.main()

