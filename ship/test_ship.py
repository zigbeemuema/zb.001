import unittest
from ship import Ship


class TestShip(unittest.TestCase):

    def setUp(self):
        self.titanic = Ship(15,10)

    def test_Ship_is_worth_it_method_for_false(self):
        
        self.assertFalse(self.titanic.is_worth_it())
        self.assertFalse(Ship(12,45).is_worth_it())
        self.assertFalse(Ship(14,67).is_worth_it())


    def test_Ship_is_worth_it_method_for_true(self):
        self.assertTrue(Ship(21,52).is_worth_it())
        self.assertTrue(Ship(23,12).is_worth_it())
        self.assertTrue(Ship(33,12).is_worth_it())


if __name__ == '__main__':
    unittest.main()


