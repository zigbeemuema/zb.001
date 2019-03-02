
class RobinHood:

    name = 'ROBINHOOD'#Initialize the name of the game

    def __init__(self,bullet=0,dragon=0):
        '''OUTPUT values of bullet and dragon'''
        self.bullet = bullet #Initialize the number of bullets
        self.dragon = dragon #Initialize the number of dragons

    def will_survive(self):
        '''OUTPUT true or false'''
        return (self.bullet / 2) >= self.dragon



if __name__ == '__main__':
    hero = RobinHood()
    hero1 = RobinHood(4,2)
    hero2 = RobinHood(2,4)
    hero3 = RobinHood(4,4)
    print(f'{RobinHood.name:^20}')
    print('hero will survive: ',hero.will_survive())  #---> True
    print('hero will survive: ',hero1.will_survive()) #---> True
    print('hero will survive: ',hero2.will_survive()) #---> False
    print('hero will survive: ',hero3.will_survive()) #---> False



