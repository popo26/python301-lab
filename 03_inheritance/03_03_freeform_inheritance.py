# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Creature():
    def __init__(self, eyes, mouth) -> None:
        self.eyes = eyes
        self.mouth = mouth

    def breathe(self):
        print("Breathe in and out.")

    def __str__(self) -> str:
        return f"This creature has {self.eyes} eyes and {self.mouth} mouth."

class Fish(Creature):
    def breathe(self):
        print("Breathe in and out in water.")

class Bird(Creature):
    def __init__(self, eyes, mouth) -> None:
        super().__init__(eyes, mouth)
        self.wings = 2
        self.beak = 1
    
    def __str__(self) -> str:
        return f"This creature has {self.eyes} eyes and {self.beak} beak. Also has beautiful {self.wings} wings instead."

giraff = Creature(2, 1)
print(giraff) 
print(giraff.breathe())    

fish = Fish(2, 1)
print(fish)
print(fish.breathe())

bird = Bird(2, 1)
print(bird)
print(bird.breathe())

