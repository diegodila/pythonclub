def calculator(x,y):
        assert isinstance(x, (int,float)), 'x precisar ser int ou float'
        assert isinstance(y, (int,float)), 'y precisar ser int ou float'
        return x + y

def soma(x,y):
        ''' Soma x e y
        >>> soma(10,20)
        30
        >>> soma(-10,20)
        10
        >>> soma('10', 20)
        Traceback (most recent call last):
        ...
        AssertionError: x precisar ser int ou float
        '''
        assert isinstance(x, (int,float)), 'x precisar ser int ou float'
        assert isinstance(y, (int,float)), 'y precisar ser int ou float'
        return x + y

if __name__ == '__main__':
        import doctest
        doctest.testmod(verbose=True)