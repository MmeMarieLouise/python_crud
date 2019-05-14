import unittest
import requests

class ApiTest(unittest.TestCase):

    def test_get_home(self):
        r = requests.get("http://127.0.0.1:5000/")
        code = r.status_code
        self.assertEqual(code, 200)


    def test_post_create(self):
        data = {'path': '~/crud', 'name': 'test-file', 'contents':'hello'}
        r = requests.post("http://127.0.0.1:5000/create", data=data)
        code = r.status_code
        text = r.text
        self.assertEqual(text, "file created")
        self.assertEqual(code, 200)
        file_object = open("~/crud/test-file", "r")
        # ensure file is there
        # ensure file has correct contents



if __name__ == '__main__':
    unittest.main()

