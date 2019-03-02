from random import randint
#Global variable for answers or responses
responses = ['It is certain','It is decidedly so','Without a doubt','Yes - definately','You may rely on it',
             'As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy, try again',
             'Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again',
             "Don't count on it",'My reply is no','My sources say no','Outlook not so good','Very doubtful']


class MagicEightBall:
    '''
        Magic Eight Ball Class
    '''

    name = 'MAGIC EIGHT BALL'#initialize name of the game

    def __init__(self):
        self.question = ''#initialize variable question to empty string
        
    def get_user_input(self):
        '''Get quetion from user'''
        response = ''
        while True:
                try:
                    response = input('Enter your question: ')
                except Exception as e:
                    print('Error: ',e)
                if response != '' and len(response) > 6 and response.endswith('?'):
                    self.question = response
                else:
                    print('Please enter a relevant question!')  
                    continue
                break   
        return self.question

    def show_progress_message(self):
        '''Output game in progress message'''
        print ('Game in progress...')

    def get_response(self):
        '''Output answer'''
        response = ''
        try:
            response = responses[randint(0,len(responses)-1)]
        except IndexError as e:
            print(e)
        return response

    def reply(self,message):
        '''Output user response'''
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

#========================================================================================


def main():

    #Display game title
    print('Welcome to {}'.format(MagicEightBall.name))

    #instantiate magiceightball 
    magicball = MagicEightBall()
    #Game status
    playing = magicball.reply('Ready to play?')

    #game on
    while playing:
        ##User enter a question
        magicball.get_user_input()

        ##Show progress message
        magicball.show_progress_message()

        ##Get answer
        print('Answer: {}\n'.format(magicball.get_response()))

        ##ask another question
        playing = magicball.reply('Ask another question/advice?')
        
    #game over
    else:
        print('Thank you for playing!!!\n')


if __name__ == '__main__':
    main()
    
    