import unittest
import requests
import tempfile
import shutil

class ApiTest(unittest.TestCase):

    # setup test temp dir
    def setUp(self):
        self.tmpDir = tempfile.mkdtemp(prefix = "pcrud")

    # destroy temp dir
    def tearDown(self):
        shutil.rmtree(self.tmpDir)

    # helper functions
    def create_test_file(self):
        myFile = open(self.tmpDir + "/test-file", "w+")
        myFile.write("hello")
        myFile.close()

    def read_test_file(self):
        file_object = open(self.tmpDir+"/test-file", "r")
        read_content = file_object.read()
        file_object.close()
        return read_content


    # test that api has a home ('/') endpoint
    def test_get_home(self):
        r = requests.get("http://127.0.0.1:5000/")
        code = r.status_code
        self.assertEqual(code, 200)

    # test that api has a create ('/create') endpoint
    def test_post_create(self):
        data = {'path': self.tmpDir, 'name': 'test-file', 'contents':'hello'}
        header = {'Content-Type': 'application/json'}
        r = requests.post("http://127.0.0.1:5000/create", json=data, headers=header)
        code = r.status_code
        text = r.text
        self.assertEqual(code, 200)
        self.assertEqual(text, "File created")
        read_content = self.read_test_file()
        self.assertEqual(read_content, "hello")

    # test that api has a read ('/read') endpoint
    def test_get_read(self):
        self.create_test_file()
        data = {'path': self.tmpDir, 'name': 'test-file'}
        header = {'Content-Type': 'application/json'}
        r = requests.get("http://127.0.0.1:5000/read", json=data, headers=header)
        code = r.status_code
        text = r.text
        self.assertEqual(code, 200)
        self.assertEqual(text, "hello")

    # test that api has an update ('/update') endpoint
    def test_post_update(self):
        self.create_test_file()
        read_content = self.read_test_file()
        self.assertEqual(read_content, "hello")
        data = {'path': self.tmpDir, 'name': 'test-file', 'contents':'goodbye'}
        header = {'Content-Type': 'application/json'}
        r = requests.post("http://127.0.0.1:5000/update", json=data, headers=header)
        code = r.status_code
        text = r.text
        self.assertEqual(code, 200)
        self.assertEqual(text, "File updated")
        read_content = self.read_test_file()
        self.assertEqual(read_content, "goodbye")

if __name__ == '__main__':
    unittest.main()

