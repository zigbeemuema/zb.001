
class Ship:
    '''
        Ship class
    '''
    name = 'Ahoy Matey'

    def __init__(self,draft=0,crew=0):
        self.draft = draft #initialize draft
        self.crew = crew #initialize crew

    def is_worth_it(self):
        '''
            Check whether ship is worth looting
        '''
        return self.draft > 20


if __name__ == '__main__':
    Titanic = Ship(15,10)
    print(f'{Ship.name}')
    print(Titanic.is_worth_it()) #---> False
