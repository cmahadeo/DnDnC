

if __name__ == '__main__':
    
    # READ A FILE
    f = open('sample.txt', "r")
    f_str = f.read()
    
    # WRITE A FILE
    g = open('sample2.txt', "w")
    g.write("Hello!\n")
    g.write("BYE!")
    
    g.close()
    
    # Formatted string literals
    # {} around strings denotes variable
    maid = 'Kanna'
    statement = f'I love {maid}!'
    print(statement)
    
    # Better to use .format
    x = 'love'
    y = 'Kanna'
    statement2 = 'I {0} {1}!'.format(x,y)
    print(statement2)
    
    # Spacing
    for x in range(1,11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))
    
    L = ['STR', 'AGI', 'INT', 'CHAR']
    for i in range(len(L)):
        print('{0:4} : {1:3d}'.format(L[i], i**6))
        
    # Here, 4 is the string length block, for which the string starts after
    # 3d is the decimal block, where each number is right-aligned
    