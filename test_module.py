import unittest
from functions import gen_to_list, division, int_division, dict_division


class TestFunctions(unittest.TestCase):

    def setUp(self):  # Initialized before every single test
        self.number = 5

    def test_gen_to_list(self):
        self.number = 4  # overwrites the setup
        self.assertEqual(gen_to_list(self.number), [0, 1.0, 2, 3])
        self.assertNotEqual(gen_to_list(self.number), [0, 1, 2, 3, 4])

    def test_division(self):
        self.assertEqual(division(5, 1), 5)
        self.assertEqual(division(4, 0),
                         None)  # There is no result in dividing 4 by 0, hence comparing to none. See func definition
        self.assertEqual(division(5, 2), 2.5)

    def test_int_division(self):
        self.assertEqual(int_division(5, 2), 2)

    def test_dict_division(self):
        dictionary = {"a": 4, "b": 2}
        self.assertEqual(dict_division(**dictionary), {"a": 4, "b": 2, "r": 2})

    def test_filter(self):  # testing a lambda anonymous function
        self.assertEqual(list(filter(lambda x: x > 3, range(7))), [4, 5, 6])


if __name__ == '__main__':
    unittest.main()
