import unittest
from robinhood import RobinHood

class TestRobinHood(unittest.TestCase):

    def setUp(self):
        self.hero = RobinHood()

    def test_robinhood_method__init__(self):
       if not self.assertIsNone (self.hero.__init__()):
            print('__init__() successfull')
       else:
            print('__init__() failed')

    def test_robinhood_method_will_survive(self):
        self.assertTrue(RobinHood().will_survive())
        self.assertTrue(RobinHood(4,2).will_survive())
        self.assertFalse(RobinHood(2,4).will_survive())
        self.assertFalse(RobinHood(12,12).will_survive())


if __name__ == '__main__':
    unittest.main()