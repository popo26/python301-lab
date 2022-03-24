# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.


try:
    num_divided = int(input("Enter a number to be divided: "))
    num_to_divide_with = int(input("Enter another number to divide with: "))
    result = num_divided / num_to_divide_with
    print(result)
except ZeroDivisionError:
    print("zero can't divide numbers.")
except ValueError:
    print("That was not number.")