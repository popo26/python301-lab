# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?


###Ai finds indentation confusing!!###

#war_and_peace
def file():
    try:
        with open("/war_and_peace.txt", "r") as file:       
            story = file.readline()
            # print(story[0])
    except FileNotFoundError: #In case user enter wrong file path
        print("Correct file path is books/war_and_peace.txt")
    else:
            print(story[0])

 

#pride_and_prejudice
def file2():
    with open("books/pride_and_prejudice.txt", "r") as file2:
        story2 = file2.readline()
        try:
            print(story2(0))
        except TypeError: # In ccase user used bracket instead of square bracket
            print("You used (0) but correct one is [0].When you get a chance revise your code.")
            print(story2[0])



#crime_and_punishment
def file3():
    with open("books/crime_and_punishment.txt", "w") as file3:
        story3 = file3.write("")
        try:
            print(story3[0])
        except TypeError: #Since there is input, it can't find anything.
            print("Empty so no word to pick up.")
            

file()
file2()
file3()


