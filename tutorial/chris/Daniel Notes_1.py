#Module


if __name__ == '__main__':
    
# script
# this is a comment
# this is a continuation of a comment

# Mutable Class

#I nteger Stuff    
    x = 5
    y = 2
    z = x+y
    u = x*y
    v = x**y
    e,f= 8, 9
    print(x,y)
    type(x)
    print(type(x))
    
# Boolean
    T = True
    F = False
    
# Going between int and bool
    
    I = int(T)
    J = int(F)
    
    K = bool(1)
    L = bool(0)
    
    # Is x equal to y?
    print(x == y)
    
    # What does == do?
    # LHS == RHS : outputs a boolean object
    # Logistic Operators: ==, OR, AND, !=
    
    result = (x == y)
    result2 = (x<=y)
    result3 = (x != y)
    result4 = (x == y) or (x != y)
    result5 = (x == y) and ( x!= y)
    
    
    # Float
    a = 1.0
    b = 1
    c = round(a)
    
    
    # Tuple
    X = (1, 2, 3, 4)
    Y = (1, 2.0, False)
    
    # doesn't give a shit about what type of objects the enties are
    
    Z = Y[0]
    W =Y[1]
    U = Y[-1]
    V = Y[-2]
    
    # negative indicies counts backwards from the end
    
    # None type
    q = None
    
    # Mutable Classes
    
    # Strings
    kanna = 'dragon maid'
    print(kanna)
    tohru = 'big breast dragon maid'
    is_kanna_big = (kanna == tohru)
    Kanna = 'loli dragon maid'
    # Python is case sensitive
    print( Kanna == kanna)
    
    m = kanna.upper()
    
    # Lists
    dragon_maids = ['Kanna', 'Tohru']
    first_maid = dragon_maids[0]
    print(dragon_maids)
    # pretty much the same as Tuple but comes with Methods
    # Elma is introduced as a dragon maid
    dragon_maids.append('Elma')
    print(dragon_maids)
    dragon_maids.reverse()
    print(dragon_maids)
    
    # String are pretty much a list of letter
    first_letter = kanna[0]
    first_word = kanna[0:6] #[1,6) half-open interval
    # y = kanna[ :] y is a copy of kanna
    
    # Dictionary
    # 'key': 'value'
    # item = (key, value)
    dragon_book = {'Kanna': 'loli maid', 'Tohru': 'Kobayashi waifu', 'Elma': 'homeless maid'}
    dragon_book['Lucoa'] = 'world class'
    dragon_book['Kobayashi'] = 'not a dragon maid'
    #dictionary[key] --> item
    
    # Dictionary Methods
    dragon_keys = dragon_book.keys()
    # returns list of keys
    dragon_items = dragon_book.values()
    # return list of items
    
    
    
    # Immutable
    p = 5
    print(id(p))
    
    p = 2
    print(id(p))
    # address gets changed
    
    # Mutable
    maids = ['Kanna', 'Tohru']
    print(id(maids))
    
    maids.append('Elma')
    maids.reverse()
    print(id(maids))
    
    # address doesnt get changed