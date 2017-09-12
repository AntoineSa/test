import unittest
from tre import mini_maxi, fill_field, erase_dobles

class minMmaxiTest(unittest.TestCase):
    def setUp(self):
        self.a, self.b = mini_maxi(5,3)

    def test_minimax (self):
        self.assertTrue(self.a < self.b)

class fillFieldTest(unittest.TestCase):
    def setUp(self):
        list = []
        self.list = fill_field(0, 3, list, "123")

    def test_fill_field(self):
        self.assertEqual(self.list, ['1','2','3'])

class eraseDoblesTest(unittest.TestCase):
    def setUp(self):
        self.field, self.l = erase_dobles(0, 1, 3, ['1','1','3'])
        

    def test_erase_dobles(self):
        self.assertEqual(self.field, ['1','3'])

if __name__ == '__main__':
    unittest.main()

exit()
