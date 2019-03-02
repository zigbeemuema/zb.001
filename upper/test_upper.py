import unittest
from upper import Upper

class TestUpper(unittest.TestCase):

    def setUp(self):
        self.upper = Upper()

    def test_Upper_is_uppercase_method_for_false(self):
        self.assertFalse(self.upper.is_uppercase('c'))
        self.assertFalse(self.upper.is_uppercase('hello I AM DONALD'))
        self.assertFalse(self.upper.is_uppercase('ACSKLDFJSgSKLDFJSKLDFJ'))
        self.assertFalse(self.upper.is_uppercase('%*&#()%&^#'))

    def test_Upper_is_uppercase_method_for_true(self):
        self.assertTrue(self.upper.is_uppercase('C'))
        self.assertTrue(self.upper.is_uppercase('HELLO I AM DONALD'))
        self.assertTrue(self.upper.is_uppercase('ACSKLDFJSGSKLDFJSKLDFJ'))



if __name__ == '__main__':
    unittest.main()