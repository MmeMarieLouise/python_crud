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
        data = {'path': self.tmpDir, 'name': 'test-file', 'contents':'hello'}
        header = {'Content-Type': 'application/json'}
        r = requests.post("http://127.0.0.1:5000/create", json=data, headers=header)
        code = r.status_code
        text = r.text
        self.assertEqual(text, "file created")
        self.assertEqual(code, 200)
        file_object = open(self.tmpDir+"/test-file", "r")
        read_content = file_object.read()
        file_object.close()
        self.assertEqual(read_content, "hello")


if __name__ == '__main__':
    unittest.main()

