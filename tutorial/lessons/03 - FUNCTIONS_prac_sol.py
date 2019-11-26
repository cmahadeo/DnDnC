# WRITE THE FOLLOWING FUNCTIONS. EACH FUNCTION IS AN ALREADY EXISTING METHOD.

# USE len(L), OR len(s), for loops, if statements, d.keys()

def is_digit(s):
    '''
    Given s is a string, returns True if every character in s is a digit. False otherwise.
    This is the same as s.isdigit()
    '''
    #i = 0
    L = ['0','1','2','3','4','5','6','7','8','9'] # defining list of all possible 1 character numbers
    #for x in s:
    for n in range(len(s)):    # better to use range than x in s
        #if type(x) == int:
        if s[n] not in L:
           #i = i + 0
            return False
        
    return True
   #     else:
   #         i = i + 1
   # if i > 0:
   #     return False
   # else:
   #     return True


def separate(s):
    '''
    Given a string of two words separated by a space, returns a tuple of the two individual words as strings.
    This is the same as s.split(' ')
    '''
    
    # Good answer
    index = 0
    
    # Find the index of the white space
    for n in range(len(s)):
        if s[n] == ' ':
            index = n
            break # Exit loop with first white space
    
    word1 = s[:index]
    word2 = s[index+1:]
    
    return (word1, word2)
        
    
    # not perfect
    #word_one = ''
    #word_two = ''
    
    #for n in range(len(s)):                       
    #    if s[n] == ' ':
    #        for i in range(0,n):
    #            word_one += s[i]
    #        for i in range(n+1,len(s)):
    #            word_two += s[i]
                
    #L = (word_one, word_two)
    
    # not correct
    #for n in range(0,len(s)):
    #    if s[n] == ' ':
    #        for i in range(0,n): 
    #            L.append(s[i])
    #        for i in range(n+1,len(s)):
    #            L.append(s[i])
    #return L


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
    for y in L:
        if y == x:
            i = i +1   # Can also write i += 1
    return i


def pop_list(L, i):
    '''
    Given L is a list, removes the item at index i of L. Returns a copy of L with x removed, with all other
    elements in the same order. This is similar to L.pop(i).
    '''
    # More correct answer
    L_pop = []
    for j in range(len(L)):
        if j != i: # Hits all indices except for i
            L_pop.append(L[j])
    
    # Good but not perfect
    M = []
    for n in range(0,i):
        M.append(L[n])
         
    for n in range(i+1,len(L)):
        M.append(L[n])
    
    return M


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

