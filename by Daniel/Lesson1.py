
if __name__ == '__main__':
    
    # Scenario number
    question = 6
    
    # IMMUTABILITY
    if question == 1:
        x = 1
        y = x
        x = 2
        print(id(x) == id(y))
    
    # MUTABILITY
    elif question == 2:
        x = [1,2,3]
        y = x
        y.append(4)
        
        print(id(x) == id(y))
        print(x)
    
    # MUTABILITY DUPLICATING
    elif question == 3:
        x = [1,2,3]
        y = x[:]
        y.append(4)
        
        print(id(x) == id(y))
        print(x)
        
    # SWAPPING ELEMENTS IN LISTS
    elif question == 4:
        x = [1,2,3,4,5]
        x[0], x[-1] = x[-1], x[0]
        
        print(x)
    
    # LISTS IN LISTS (DO NOT GO BEYOND 1 EMBEDDING)
    elif question == 5:
        x = [[1,2], [3,4]]
        print(x[0][1])
        print(x[1][0])
    
    # LOGIC (DO NOT USE BOOLEAN STATEMENTS ON MUTABLE OBJECTS, EXCEPT SHORT STRINGS)
    # DO NOT USE BOOLEAN STATEMENTS ON DIFFERENT CLASSES
    elif question == 6:
        L = [1,2,3,4,5]
        x = 6
        
        print(x in L or x > 4)
        print(x in L and x > 4)
        
    else:
        pass

