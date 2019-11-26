
if __name__ == '__main__':
    
    if False:
        # TRIVIAL IF STATEMENT
        if True:
            print("Trivial if statement")
        
    
        # AN OPERAND IF STATEMENT
        x = 0
        if x > 0:
            print("x is positive")
        
        elif x > -1:
            print("x is greater than -1")
        
        elif x  > -2:
            print("x is greater than -2")
        
        else:
            print("x is none of the above")
        
    # DIFFERENT WAYS OF WRITING IF STATEMENTS:
    # Use operators == (equals), <, >, <=, >=, !=
    # Multiple Boolean statements possible with and, or, not
    
    # RULES FOR IF STATEMENTS
    if False:
        L = [1,2,3]
        x = 1
        # IN STATEMENT
        if x in L:
            print("x is in the list!")
            
        
        y = 0.5
        if (y > 0.0) and (y > 1.0):
            print("Condition 1")
        else:
            print("Else condition")
            
    
    

    
    # TRY STATEMENT
    kanna = 'dragon maid'
    try:
        print(kanna)
    except NameError:
        print("Kanna is not defined wtf???")
    except ValueError:
        print("Kanna has the wrong value!")
    else:
        print("Kanna is defined yay!")
        
        
    # LOOPS
    
    done = False
    num = 0
    while not done:
        
        if num < 10:
            print("This is not the end!")
            num += 1
        
        else:
            done = True
    
    # FOR LOOP (needs a list!)
    L = [1,2,3,4]
    for x in L:
        print(x)
            
    # STARTING HERE:
    k = 1
    while k <= 4:
        print(k)
        k += 1    
        
        