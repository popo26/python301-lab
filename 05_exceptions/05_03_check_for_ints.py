# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.


is_on = True

while is_on:
    try:
        user_reply = int(input("Enter an integer: "))
        if user_reply == type(int):
            print("user_reply")
        is_on = False

    except ValueError:
        print("that is not an integer.")

