# MODULE

# global a, b

def f(x):
    '''
    This function takes a number x, and returns its square value.
    
    1. What are the arguments, and their types? x is a float, or int type.
    2. What does your function do? Squares x!
    3. What does your function output? Returns the square of x.
    '''
    
    
    # BEHIND THE SCENES: x (local) = a (global)
    # Local variables only exist within the function!
    
    # What is x here?
    # x has the same VALUE as a. BUT! It is a different variable.
    
    # AFTER RETURN, DESTROY x (local)
    return x**2

# Naming functions is the same as variables.
# Some valid names

def get_square(x):
    '''
    '''
    
    pass


# Put two linebreaks in between each line.
def get_square_root(x):
    '''
    '''
    
    # pass means empty line, so python just reads and continues.
    # Basically, I'm lazy and I haven't written this function yet.
    pass


# Functions do not need return.

def print_str(x):
    '''
    Prints x.
    '''
    
    print(x)
    # Putting nothing is the same as writing:
    return None


# MUTABLE VS IMMUTABLE CLASSES
# Every python function takes a variable input, and does a pass by value.

# Functions can:
 # Change values of the argument
 # Return values by processing the argument values
# DOES THE FUNCTION CHANGE THE VALUE OF THE ARGUMENT?
 # With mutable, the global variable's value gets changed.
 # With immutable, nothing happens to the global variable's value.

def get_first(L):
    '''
    Return the first element of L.
    '''
    
    return L[0]


def add_element(L):
    '''
    L is a list.
    '''
    
    # L (local) = K (global)
    L.append(4)
    return None


def change_int(x):
    '''
    x is an integer. We are trying to change x.
    '''
    
    # x (local) = b (global)
    x = 1
    return x

# WAYS TO FORMAT ARGUMENTS:
def multi_f(x, y, z):
    '''
    Multivariate function.
    '''
    
    return 2*x*y*z**2


# NO ARGUMENT
def noarg_f():
    '''
    Prints some random shit.
    '''
    
    print("I LOVE KANNA")
    return 0
    
# KEYWORD ARGUMENTS
def key_f(x, y=2, z=3):
    '''
    Accepts x as an argument, with default value x = 1.
    '''
    
    return 2*x*y*z


# STARRED ARGUMENTS
def kanna(*args):
    '''
    *args takes as many arguments as you want, and accepts all of them as a tuple.
    '''
    
    # Here, args is a tuple. len(args) is the number of arguments you have.
    if len(args) == 0:
        pass
    
    elif len(args) == 1:
        print(args[0])
    
    elif len(args) == 2:
        print(args[0])
        print(args[1])
    
    else:
        print(args[0])
        print(args[1])
        print(args[2])
    
    return None


def size(**kwargs):
    '''
    **kwargs takes as many keyword arguments as you want, and accepts all of them as a dict.
    '''
    
    # Define a default dictionary
    all_args = {'oppai': 'big'}
    
    for key in all_args.keys():
        if key in kwargs.keys():
            all_args[key] = kwargs[key]
            
    
    # Here, use all_args as your argument dictionary
    if 'oppai' in all_args.keys():
        print(all_args['oppai'])
    
    return None


# Normal arguments, then keywords
# Normal, then starred.
def big_f(x, y, *args, z=2, **kwargs):
    '''
    x, y are arguments that are needed, z = keyword, etc. *args are additional arguments, **kwargs
    '''
    
    return 2*x*y*z


def g(x):
    '''
    Returns some quadratic.
    '''
    
    return (x**2 + x + 2)


if __name__ == '__main__':
    # b = 2 # Global variable b
    # change_int(b)
    # print(b)
    # print(x)
    
    # This is the same as:
    # x = b # I'm giving x, b's value
    # x = 1 # I'm changing x's value.
    # print(b)
    
    # K = [1,2,3]
    # a = get_first(K)
    # print(K)
    
    # a = (1,2,3)
    # h = multi_f(*a)
    # a = noarg_f()
    
    # b = key_f(3, y=3, z=4)
    # a = (1,2,3)
    # kanna(a)
    # kanna(*a)
    
    d = {'oppai': 'big',
         'kanna': 'loli',
         'kobayashi': 'mom'
         }
         
    # size(oppai='big', kanna='loli', kobayashi='mom')
    # size(**d)
    
    # z = big_f(1,2,4, z=3)
    
    # Quickly define a function. This is the same as function g(x) above.
    g = lambda x, y: x**2 + y + 2
    h = lambda x: g(x)
    
    z = g(2,3)