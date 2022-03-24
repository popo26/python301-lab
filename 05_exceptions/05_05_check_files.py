# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.


##Ai not getting it

file_name = "integer.txt"

try:
    with open(file_name, "r") as file:
        num = file.readline()
        first_num = num.strip()
        print(first_num)
        for n in file:
            sum = 0
            sum = int(first_num) + int(n)
            print(sum)
        
except IOError:    
    print("right file path?")
       
except ValueError:
    print("right data type?")

except:#Catching no error message
    print("Not calculating correctly.")







        


    
   
    


 