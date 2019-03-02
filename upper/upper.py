
class Upper(object):
    '''
    Upper Class
    '''
    name = 'UPPER'

    def is_uppercase(self,text):
        ''' 
            Check whether text is all upper case
        '''
        return text.isupper()



if __name__ == '__main__':
    
    print(f'{Upper.name}')
    print(Upper().is_uppercase('c'))                      #---> False
    print(Upper().is_uppercase('C'))                      #---> True
    print(Upper().is_uppercase('hello i AM DOLNAD'))      #---> False
    print(Upper().is_uppercase('HELLO I AM DOLNAD'))      #---> True
    print(Upper().is_uppercase('ACSKLDFJSgSKLDFJSKLDFJ')) #---> False
    print(Upper().is_uppercase('ACSKLDFJSGSKLDFJSKLDFJ')) #---> True




