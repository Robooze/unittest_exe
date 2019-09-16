import unittest
from list_function import gen_to_list


class TestGenConversion(unittest.TestCase):

    def setUp(self):
        self.number = 5

    def test_gen_to_list(self):
        self.number = 4
        self.assertEqual(gen_to_list(self.number), [0, 1, 2, 3])

    def test_2nd_gen_to_list(self):
        self.assertNotEqual(gen_to_list(self.number), [0, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
