#unit test
from operator import add
import unittest
import main_test


class TestGame(unittest.TestCase):
    def test_input(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_main_test(self):
        self.assertEqual(main_test.some_function(), "Hello, World!" )

if __name__ == '__main__':
    unittest.main()