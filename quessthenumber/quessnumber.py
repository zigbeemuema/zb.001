from random import randint

playing = True #Global variable to check status of the game

class QuessNumber:
    '''
        Quess the number game
    '''
    name = 'QUESS THE NUMBER' #name of the game
    limit = 5 #limit of playing 

    def __init__(self):
        '''initialize self.life'''
        self.life = QuessNumber.limit
        self.trials = 0

    def reset_life_and_trial(self):
        '''Restore the value of self.life and self.trials'''
        self.__init__()

    def user_input(self):
        '''OUTPUT user number'''
        number = 0 #user input number
        while True:
            try:
                number = int(input('Enter a number:'))
                self.trials += 1
                if self.trials >= QuessNumber.limit:
                    raise Exception('Sorry number of trials exceeded limit!!!\n'.upper())
            except ValueError:
                print('Error: please enter an integer!!!')
                continue
            except Exception as e:
                print(e)
                break
            else:
                break
        return number
    def get_number(self):
        '''OUTPUT the random number'''
        return randint(0,1000) #the random number

    def lose_life(self):
        '''OUTPUT self.life - 1'''
        if self.life > 0:
            self.life -= 1

    def earn_life(self):
        '''OUTPUT self.life '''
        self.life 

#==============================================================================

def check_number(quessnumber):
    '''Check number output boolean (True or False)'''
    if quessnumber.get_number() == quessnumber.user_input():
        quessnumber.earn_life()
        return True
    else:
        quessnumber.lose_life()
        return False

def reply(message):
    '''Take user response output boolean (True or False)'''
    response = ''
    while True:
            try:
                response = input('{} Y/n: '.format(message))
            except Exception as e:
                print('Error: ',e)
            if response.lower().startswith('y'):
                return True
            elif response.lower().startswith('n'):
                return False 
            else:
                print('Please enter y or n!')  
                continue
            break   
        
def main():
    '''Game driver or main function'''
    #Title of the game
    print('Welcome to {}'.format(QuessNumber.name))

    #Check whether user wants to play
    playing = reply('Ready to play?')
    #instantiate the QuessNumber class
    quessnumber = QuessNumber()
    #Start playing
    while playing:
        ##ask user for number and Check the number
        if check_number(quessnumber):
            ###Player won
            if quessnumber.trials != QuessNumber.limit:
                print('CONGRATULATIONS YOU WON WITH {} LIFES'.format(quessnumber.life))
            playing = reply('Play again?')
            quessnumber.reset_life_and_trial()
        else:
            ###Player lost
            if (quessnumber.life == 0):
                playing = reply('Play again?')
                quessnumber.reset_life_and_trial()
            else:
                print('Sorry You failed! you have {} lifes remaining'.format(quessnumber.life))
    #Stop playing
    else:
        print('Thank you for playing!!!!\n')
    

#run the game
if __name__ == '__main__':
    main()
   
        
    