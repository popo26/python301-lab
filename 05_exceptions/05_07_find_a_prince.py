# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".



class PrinceException(Exception):

    def __str__(self):
        return "Yes there is a Prince!"

#Change the file path to check Prince in other files.

with open("books/war_and_peace.txt", "r") as file:
    story = file.read()
    first100 = story[0:100] # To get first 100 characters
    try:
        if "Prince" in first100:
            raise PrinceException
    except PrinceException as p:
        print(p)
    else:
        print("There is no Prince.")