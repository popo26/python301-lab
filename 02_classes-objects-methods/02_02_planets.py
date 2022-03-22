# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    def __init__(self, color, temp, creature):
        self.color = color
        self.temp = temp
        self.creature = creature

    # def description(self):
    #     print(f"This {self.color} planet is found. The temperature is {self.temp} degrees.\nThere are few {self.creature}s detected.")

    def __str__(self):
        return f"This {self.color} planet is found. The temperature is {self.temp} degrees.\nThere are few {self.creature}s detected."


p = Planet("red", 200, "giraff")
print(p)
# output = p.description()
# print(output)
