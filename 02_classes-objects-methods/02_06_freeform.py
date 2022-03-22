# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Person():
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def __add__(self, other):
        new_name = "Nana" + " " + self.name + other.name
        new_age = self.age + other.age
        new_hobby = "tiny bit of " + self.hobby + "and " + other.hobby
        return Person(name=new_name, age=new_age, hobby=new_hobby )

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old. {self.name}'s hobby is {self.hobby}."
        

class School():
    def __init__(self, school_name, level, commute_method) -> None:
        self.name = school_name
        self.level = level
        self.method = commute_method

    def __str__(self) -> str:
        return f"{self.name} is a {self.level}. You go to {self.name} by {self.method}"

class Work():
    def __init__(self, job, start_time, fatigue_level) -> None:
        self.job = job
        self.start = start_time
        self.fatigue = fatigue_level

    def __str__(self) -> str:
        return f"{self.job} job starts at {self.start} am. At the end of the day, you are {self.fatigue} "

coco = Person("Coco", "18", "shopping")
kirin = Person("Kirin", "6", "imagining")
new = coco + kirin
print(coco)
print(kirin)
print(new)

primary = School("Glamorgan", "primary school", "walking")
high_school = School("Westlake", "high school", "driving")
print(primary)
print(high_school)

operator = Work("machine operator", 7, "super tired")
student = Work("student", 6, "mentally tired")
print(operator)
print(student)
        


