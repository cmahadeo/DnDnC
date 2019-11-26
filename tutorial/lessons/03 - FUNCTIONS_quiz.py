# WHAT HAPPENS TO THE ORIGINAL ARGUMENT AFTER EACH FUNCTION IS PASSED?

def f(x):
    '''
    x is an integer.
    '''
    
    x = 2
    return None


def f2(x):
    '''
    x is an integer.
    '''
    
    # print(id(x (local)))
    print(id(x)) # Is this ID the same as global ID? This x is not the same variable as argument x
    return x


def f3(L):
    '''
    L is a list.
    '''
    
    # L (local) = L (global)
    print(id(L))
    L = [] # This doesn't affect L (global) value. 
    
    return L


def f4(L):
    '''
    L is a list.
    '''
    
    L = L + [4] # Never do this! Use L.append(4) instead!
    print(id(L))
    return None


def f5(L):
    '''
    L is a list.
    '''
    
    L.append(4) # This is the right way. Always change lists and dicts using methods.
    print(id(L))
    return None


def f6(x):
    '''
    x is an integer.
    '''
    
    y = f6_2(x) # x = 2 => y = 4
    return y


def f6_2(x):
    '''
    x is an integer.
    '''
    
    return x**2 # 4


if __name__ == '__main__':
    
    test = 'f6'
    
    if test == 'f':
        x = 3
        f(x)
        print(x)
    
    elif test == 'f2':
        x = 3
        print(id(x))
        y = f2(x)
        print(id(y))
        
        # Memory address is not affected if you're not changing the value!
    
    elif test == 'f3':
        L = [1,2,3]
        print(id(L))
        L2 = f3(L)
        print(id(L2))
        print(L)
        print(L2)
        
    elif test == 'f4':
        L = [1,2,3]
        print(id(L))
        f4(L)
        print(L)
        
    elif test == 'f5':
        L = [1,2,3]
        print(id(L))
        f5(L)
        print(L)
        
    elif test == 'f6':
        x = 2
        z = f6(x) # Does this work?
        