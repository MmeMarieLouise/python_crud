import unittest
import requests
import tempfile
import shutil

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.tmpDir = tempfile.mkdtemp(prefix = "pcrud")

    def tearDown(self):
        shutil.rmtree(self.tmpDir)

    def test_get_home(self):
        r = requests.get("http://127.0.0.1:5000/")
        code = r.status_code
        self.assertEqual(code, 200)

    def test_post_create(self):
        code, text = self.make_create_request()
        self.assertEqual(text, "file created")
        self.assertEqual(code, 200)
        file_object = open(self.tmpDir+"/test-file", "r")
        read_content = file_object.read()
        file_object.close()
        self.assertEqual(read_content, "hello")

    def test_get_read(self):
        code, _ = self.make_create_request()
        self.assertEqual(code, 200)
        data = {'path': self.tmpDir, 'name': 'test-file'}
        header = {'Content-Type': 'application/json'}
        r = requests.get("http://127.0.0.1:5000/read", json=data, headers=header)
        code = r.status_code
        text = r.text
        self.assertEqual(code, 200)
        self.assertEqual(text, "hello")

    def make_create_request(self):
        data = {'path': self.tmpDir, 'name': 'test-file', 'contents':'hello'}
        header = {'Content-Type': 'application/json'}
        r = requests.post("http://127.0.0.1:5000/create", json=data, headers=header)
        code = r.status_code
        text = r.text
        return code, text

if __name__ == '__main__':
    unittest.main()

