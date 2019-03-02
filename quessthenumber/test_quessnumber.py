import unittest
from quessnumber import *

class TestQuessNumber(unittest.TestCase):
    def setUp(self):
        self.quessnumber = QuessNumber()

    def test_quessnumber_method__init__(self):
        if not self.assertIsNone (self.quessnumber.__init__()):
            print('__init__() successfull')
        else:
            print('__init__() failed')

    def test_quessnumber_method_reset_life_and_trial(self):
        if not self.assertIsNone (self.quessnumber.reset_life_and_trial()):
            print('reset_life_and_trial() successfull')
        else:
            print('reset_life_and_trial() failed')

    def test_quessnumber_method_user_input_when_input_is_correct(self):
        number = self.quessnumber.user_input()
        if isinstance(number,int): 
            number =  True
            self.assertTrue(number)
            print('user_input() successful')
        else:
            self.assertRaises(ValueError,self.quessnumber.user_input(),number)
            print('user_input() failed')

    def test_quessnumber_method_get_number(self):
        number = self.quessnumber.get_number()
        if number:
            number = True
            print('get_number() successful')
            self.assertTrue(number)
        else:
            number = False
            print('get_number() failed')
            self.assertFalse(number)

    def test_quessnumber_method_lose_life(self):
        
        if not self.assertIsNone (self.quessnumber.lose_life()):
            print('lose_life() successful')
        else:
            print('lose_life() failed')
            
    def test_quessnumber_method_earn_life(self):
        if not self.assertIsNone (self.quessnumber.earn_life()):
            print('earn_life() successful')
        else:
            print('earn_life() failed')

    def test_check_number(self):
        status = check_number(self.quessnumber)
        if (status):
            print('CONGRATULATIONS YOU WON')
            self.assertTrue(status)
        else:
            print('Sorry You failed!')
            self.assertFalse(status) 


    def test_reply(self):
       answer = reply('Ready to play?')
       if answer == True:
           print('playing = true')
           self.assertTrue(answer)
       else:
            print('playing = false')
            self.assertFalse(answer) 

    def test_main(self):
        test = self.quessnumber

        if test:
            test = True
            print('test successful')
            self.assertTrue(test)
        else:
            print('test failed')
            self.assertFalse(test)

if __name__ == '__main__':
    unittest.main()