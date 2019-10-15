# WRITE THE FOLLOWING FUNCTIONS. EACH FUNCTION IS AN ALREADY EXISTING METHOD.

# USE len(L), OR len(s), for loops, if statements, d.keys()

def is_digit(s):
    '''
    Given s is a string, returns True if every character in s is a digit. False otherwise.
    This is the same as s.isdigit()
    '''
    i = 0
    for x in s:
        if type(x) == int:
           i = i + 0
        else:
            i = i + 1
    if i > 0:
        print(False)
    else:
        print(True)
    
    
    return None


def separate(s):
    '''
    Given a string of two words separated by a space, returns a tuple of the two individual words as strings.
    This is the same as s.split(' ')
    '''
    L = []
    for n in range(0,len(s)):
        if s[n] == ' ':
            for i in range(0,n):
                L.append(s[i])
            for i in range(n+1,len(s)):
                L.append(s[i])
    return L


def dict_copy(d):
    '''
    Given d is any dictionary, returns a copy of d (with a different memory address).
    This is the same as d.copy()
    '''
    
    return None


def count(L, x):
    '''
    Given L is a list, x is any value, returns the number of occurances of x in L.
    This is the same as L.count(x).
    '''
    i = 0
    for n in L:
        if n == x:
            i = i +1
    return i


def pop_list(L, i):
    '''
    Given L is a list, removes the item at index i of L. Returns a copy of L with x removed, with all other
    elements in the same order. This is similar to L.pop(i).
    '''
   
   #M = []
    #for n in range(0,i):
     #   M.append(L[n])
         
    #for n in range(i+1,len(L)):
     #   M.append(L[n])
    
   #return M


def make_range(*args):
    '''
    Given each arg is an integer:
    - If args = (stop): Return a list of all integers from 0 to stop (exclusive)
    - If args = (start, stop): Returns a list of all integers from start (inclusive) to stop (exclusive)
    - If args = (start, stop, step): Returns a list of all integers step apart from start (inclusive) to stop (exclusive)
    
    All additional arguments past the first 3 are ignored. This is similar to range(*args).
    '''
    
    return None


def make_dict(key, **kwargs):
    '''
    Returns a dictionary of all kwargs, with the exception of key.
    '''
    
    return None


if __name__ == '__main__':
    pass

