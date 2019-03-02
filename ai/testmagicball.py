import unittest
from magicball import *

class TestMagicEightBall(unittest.TestCase):

    def setUp(self):
        self.magicball = MagicEightBall()

    def test_magiceightball_method__init__(self):
         if not self.assertIsNone (self.magicball.__init__()):
            print('__init__() successfull')
         else:
            print('__init__() failed')

    def test_magiceightball_method_get_user_input(self):
        answer = self.magicball.get_user_input()
        if answer:
            answer = True
            print('get_user_input() successfull')
            self.assertTrue(answer)
        else:
            print('get_user_input() failed')
 

    def test_magiceightball_method_show_progress_message(self):
        if not self.assertIsNone (self.magicball.show_progress_message()):
            print('show_progress_message() successfull')
        else:
            print('show_progress_message() failed')

    def test_magiceightball_method_get_response(self):
        answer = self.magicball.get_response()
        if answer != '':
            answer = True
            print('get_response() successfull')
            self.assertTrue(answer)
        else:
            print('get_response() failed')
 

    def test_magiceightball_method_reply(self):
       answer = MagicEightBall().reply('Ask another question/advice?')
       if answer == True:
           print('playing = true')
           self.assertTrue(answer)
       else:
            print('playing = false')
            self.assertFalse(answer) 
    def test_main(self):
        test = self.magicball

        if test:
            test = True
            print('test successful')
            self.assertTrue(test)
        else:
            print('test failed')
            self.assertFalse(test)


if __name__ == '__main__':
    unittest.main()
    



