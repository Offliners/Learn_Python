# creating custom exceptions
class ExceptionA(Exception): # inherits
    pass # but adds nothing

class ExceptionB(Exception):
    pass

for n in range(6):
    try:
        if n % 2:
            raise ExceptionA
        else:
            raise ExceptionB
    except ExceptionA:
        print("Exception A caught")  
    except ExceptionB:
        print("Exception B caught") 

# Output:
# Exception B caught
# Exception A caught
# Exception B caught
# Exception A caught
# Exception B caught
# Exception A caught 
