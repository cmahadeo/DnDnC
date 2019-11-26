# Compatibility with Python2
from __future__ import absolute_import

fromlib = True
import_method = 2


if not fromlib:
    # METHODS OF IMPORTING FROM mypackage.py:
    
    # Ordinary import: Imports all elements of mypackage
    if import_method == 1:
        import mypackage
    
    # Renaming import: Imports all elements and renames mypackage to mp
    elif import_method == 2:
        import mypackage as mp
        
    # Only imports the function chris_fun from mypackage
    elif import_method == 3:
        from mypackage import chris_fun

else:
    # METHODS OF IMPORTING FROM library folder mylib:
    
    # Imports all .py packages listed in __all__
    if import_method == 1:
        from mylib import *
    
    # Imports each .py file in mylib separately, renaming each
    elif import_method == 2:
        
        # Use dots instead of backslash for imports on higher directories
        # Good idea to import each package separately
        # Same as: from mylib import mypackage, mypackage2
        import mylib.mypackage1 as mp
        import mylib.mypackage2 as mp2
    
    # This method doesn't seem to work. Perhaps use importlib instead?
    elif import_method == 3:
        import mylib
    

if __name__ == '__main__':
    
    # Using the imported package with respect to each imported method
    
    if not fromlib:
        # Using mypackage.py:
        
        if import_method == 1:
            
            # Use chris_fun
            mypackage.chris_fun()
        
        
        elif import_method == 2:
            
            # Use chris_fun
            mp.chris_fun()
        
        
        elif import_method == 3:
            
            # Use chris_fun
            chris_fun()
    
    else:
        if import_method == 1:
            
            # Use each function
            mypackage1.fun1()
            mypackage2.fun2()
        
        elif import_method == 2:
            
            mp.fun1()
            mp2.fun2()
        
            
        
    
    
    

