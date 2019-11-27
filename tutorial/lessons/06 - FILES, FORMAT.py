# FINAL LESSON

# class attributes with strings
# type <file>
# string formatting (advanced)

class DragonMaid:
    
    def __init__(self):
        self.name = 'Kanna'
        self.age = 6
        self.hobbies = ['being kawaii']
        

if __name__ == '__main__':
    
    topic = 3
    
    if topic == 1:
        
        # CLASS ATTRIBUTES
        
        kanna = DragonMaid()
        
        # hasattr, getattr, setattr
        
        # hasattr
        has_name = hasattr(kanna, 'name')
        has_relation = hasattr(kanna, 'relatives')
        
        # getattr
        kanna_name = getattr(kanna, 'name') # Same as kanna_name = kanna.name
        
        # setattr (returns nothing)
        setattr(kanna, 'age', 1000) # Same as kanna.age = 1000
    
    
    elif topic == 2:
        # type file is an object type (file is a kind of iterator, see iterator objects for detail)
        
        # INITIALIZATION OF FILE
        
        # 'w' creates 'sample.txt'
        f = open('sample.txt', 'w') # 'r' for reading, 'w' for writing
        
        # Write down strings to put into our file f
        string = 'Hello World!\n'
        string2 = 'Hello World again!'
        f.write(string)
        f.write(string2)
        
        f.close() # Closes the file object f, and saves all string into sample.txt
        
        # 'r' reads 'sample2.txt'
        f2 = open('sample2.txt', 'r') # Saves string in sample2.txt into file object f2
        
        # read f2 as a string
        # f2_string = f2.read() # As a list: f2_lineslist = f2.readlines()
        
        f2_line = f2.readline()
        f2_line2 = f2.readline()
        
    
    # LAST TOPIC: FORMATTED STRING TYPE
    
    # STRINGS IN A TABLE FORMAT
    maid = 'Kanna'
    statement = f'I love {maid}' # f'' format string type
    
    person = 'Kobayashi'
    
    statement2 = f'{person} loves {maid}!'
    statement2_alt = '{0} loves {1}!'.format('Kobayashi', 'Kanna')
    statement2_alt2 = '{0} loves {1}!'.format(person, maid)
    
    # Character spacing
    attr1 = 'strength'
    attr2 = 'agility'
    
    table = '{0:10}={1:4d}'.format(attr1, 100)
    table2 = '{1:4d}={0:10}'.format(attr1, 100)
    # Creates a character block that is maximum of number 10 and len(attr1). Left-aligned!
    # Remember to write d for integers, floats. Right-aligned!
    
    # Character spacing
    L = ['STR', 'AGI', 'INT', 'CHAR']
    L_values = [10, 5, 20, 16]
    
    table3 = ''
    for i in range(len(L)):
        table3 += '{0:5} : {1:3d}\n'.format(L[i], L_values[i])
    
    print(table3)
    
    # Organize as ATTR = VALUE
    