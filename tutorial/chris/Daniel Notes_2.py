#Module


if __name__ == '__main__':
# CHECK INDENT PROBLEMS    
# script
# this is a comment
# this is a continuation of a comment
 if False:

    
    #Trivial if statement
    #if Boolean:
    #   print("Print this")
            if True:
                print("Trivial if statement")
                
            # An operand if statement
            x = 1
            if x > 0:
                print("x is positive")
            if x < 0:
                print("x is negative")
                
            y = -1
            if y > 0:
                print("y is positive")
            else:
                print("y is not positive")
                
            z = 0
            if z > 0:
                    print("z is positive")
            elif z == 0:
                    print("z is zero")
            else:
                    print("z is not positive") 
                    
            # Boolean statements don't need to be mutually exclusive
            # If loop checks for first condition that is satisfied and executes that result (ignores others)
            
            a = -1
            if a > 0:
                print("z is positive")
            elif a > -2:
                print("a is bigger than -2")
            elif a > -3:
                print("a is bigger than -3")
            else:
                print("none of the above")     
                
            # Different ways of writing IF statements:
            # use operators == (equals), >, <, <=, >=, != (not equal)
            # multiple Boolean statements possible with and, or, not
            
            r = 0.2
            
            if r > 0.1:
                print("Condition 1")
            else:
                print("Else condition 1")
                
            if (r == 0.0) or (y == 1.0):
                print("Condition 2")
            else:
                print("Else condition 2")
                
            if (r > 0.0) and (r < 1.0):
                print("Condition 3")
            else:
                print("Else condition 3") 
                
            
            L = [1,2,3]
            p = 1
            # Do not do this
            if L == []:
                print("Empty list")
            if L == [2,1,3]:
                print("Is this class the same?")
            # DO like this instead
            if p in L:
                print("p is in the list")
            
           # Try statement
                
            kanna = 'dragon maid'
            try:
             print(kanna)
            except:
             print("Kanna is not defined")
            else:
             print("Kanna is defined")            
            
            

# WHile loop

#while Boolean:
 # Script or something that involes Boolean
 
 # while True:
  #print("This never ends") #Do not run this it explodes
 
#   done = False
 #  num = 0
# 
 # while not done:
  # if num < 10:
   # print("this is not the end")
   # num += 1 # means num = num + 1
   #else:
   # done = True
 
 
 
 
# For Loop
# Needs a list

 L = [1,2,3,4]
 
 # Do not need to define x before hand
 # x is a local variable
 
 for x in L:
  print(x)
 
 for i in range(1,10): #[start, finish)
  print(i)
 
 #Starting here
 k = 1
 while k in L:
  print(k)
  k += 1
  
 # Alternatively
 while k <= 4:
  print(k)
  k += 1