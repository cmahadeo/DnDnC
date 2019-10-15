# Module


# Define functions in Module area
def f(x):
    '''
    Write your comment here.
    
    This function takes a number x and returns its square value.
    
    (Function comment)
    
    '''
    # Behind the scenes: x (local) = a (global)
    # local variables only exist within the function
    
    
    # What is x?
    # x has the same VALUE, but is a DIFFERENT variable
    
    # After return, destroy x
    return x**2

# 1. What are arguements and types? x is float or int
# 2. What does function do? Square x
# 3. What does function output? Returns square of x

# Naming functions same as variables
# Keep naming consistent
# example names

def get_square(x):
    '''
    '''
    
    # Pass means empty line. python reads and continues.
    # Basically  I am lazy and haven't written this function yet
    pass

# Two lines between each function
def get_square_root(x):
    '''
    '''
    pass

# Function doesn't need a return
def print_str(x):
    '''
    Prints x
    
    '''
    print(x)
    return None
    
# Putting nothing is equivalent to writing: return None

# Does the function change the value of the arguement?

# Does change values
def get_first(L):
    '''
    Return first element of list L
    '''
    return L[0]


# change values
def add_element(L):
    '''
    L is a list
    '''
    # L (local) = K (globa)
    L.append(4)
    # destroy L
    return None

def change_int(x):
    '''
    x is an integer
    '''
    
    x = 1
    return x

# Ways to format arguements
def multi_f(x, y, z):
    '''
    multivariate function
    '''
    
    return 2*x*y*z**2

# No arguement
def no_arg_f():
    '''
    Prints random shit
    '''
    print("I love Kanna")
    return 0
# Keyword arguments
def key_f(x=1):
    '''
    Accepts x as an arguemnt with default value x = 1
    '''
    y = x**2
    return y


# Mixed example
def key_g(x, y = 2, z = 3):
    return 2*x*y*z


# Starred Arguments
# * splits a tuple into individual arguments
def kanna(*args):
    '''
    args is any tuple
    *args breaks args into individual elements and evaluates on them all
    spits out a tuple
    '''
    
    # args is a tuple
    print(args[0])
    print(args[1])
    print(args[2])
    
    return None


# Star keyword functions
def tohru(**kwargs):
    '''
    **kwargs takes as many keyword arguements as you want and accepts all of them as a dictionary
    '''
    # Define a default dictionary
    all_args = {'oppai' : 'big'}
    for key in all_args.keys():
        if key in kwargs.keys():
            all_args[key] = kwargs[key]
    # here kwargs is a dictionary
    if 'oppai' in all_args.keys():
        print(all_args['oppai'])
        
    return None

# All in one example
def big_f(x, y, *args, z = 3, **kwargs):
    '''
    x, y are arguements that are needed, *args are additional arguments, z = keyword, **kwargs are additional keyword arguements
    order: normal arguements, *-arguements, keyword arguements, *-keyword arguements
    '''
    return 2*x*y*z


# Lamba functions
def quad(x):
    '''
    returns qudratic
    '''
    
    return (x**2 + x + 2)

if __name__ == '__main__':
    
    a = 2 # Global Variable a
    y = f(a)
    
    # Can rename functions for convenience
    g = f
    z = f(a)
    
    
    s = 'Kanna'
    print_str(s)
    
    # Immutable example
    b = 2
    change_int(b)
    print(b)
    
    # This is the same as:
    x = b # Giving x the value of b
    x = 1 # Change the value of x
    print(b)
    
    b = change_int(b)
    print(b)
    
    # Mutable example
    K = [1,2,3]
    add_element(K)
    print(K)
    print(get_first(K))
    
    #Multivariate example
    h = multi_f(2,3,4)
    
    #No argument example
    a = no_arg_f()
    
    # Keyword example
    p = key_f()
    r = key_f(x=3) # Use this to stay consistent with keyword arguements
    q = key_f(3)
    
    # Mixed arguement
    m = key_g(3)
    n = key_g(3, y=3,z=3)
    
    # Star arguement example
    kanna(1,2,3,4,5,6,7,8)
    
    # Star keyword argument
    tohru(oppai = 'big', kanna = 'loli', kobayashi = 'mom')
    
    
    # All in one example
    z = big_f(1,2)
    z1 = big_f(1,2,4, z = 5)
    
    # Lamba function example
    quad1 = lambda x: x**2 + x + 2 
    
    # defines same function as g(x) above
    # used for very short functions
    
    w = quad(2)
    print(w)
    w1 = quad1(2)
    print(w1)
    
    
    