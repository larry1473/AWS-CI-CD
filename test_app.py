import unittest
from app import sayHelleo


class TestApp(unittest.TestCase):

    def test_say_hello(self):
        self.assertEqual(sayHelleo("World"), "Hello, World!")
        self.assertEqual(sayHelleo("Alice"), "Hello, Alice!")
        

if __name__ == '__main__':
    unittest.main()