# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.


file_name = "integers.txt"

def add():
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
        print("check if file path is correct")
    except ValueError:
        print("check if the correct value is entered")



add()
            









        


    
   
    


 