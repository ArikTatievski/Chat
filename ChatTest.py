import unittest
from ClientSide import *
from ServerSide import *

class MyTestCase(unittest.TestCase):
    def test_login(self):
        Server()
        x = Client('192.168.56.1','100000','Arik')
    def test_private_msg(self):
        self.assertEqual(True, True)  # add assertion here
    def test_download_file(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

