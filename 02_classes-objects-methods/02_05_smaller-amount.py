# Update the __add__() method of `Ingredient()` so that instead of
# instantiating the new Ingredient() object with an amount of 1,
# it'll take whichever amount of the passed ingredients is smaller
#
# Example:
# c = Ingredient("carrot", 5)
# p = Ingredient("pea", 4)
# s = c + p
# print(s)
# >>> OUTPUT: carrotpea (4)

class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + other.name
        new_amount = min(self.amount, other.amount)
        return Ingredient(name=new_name, amount=new_amount)
    
    def __str__(self): # for end-user more clarity when using print() on an Ingredient() object. If __str__() doesn't exist fall back to _-repr__()
        return f"{self.name} ({self.amount})"
    
    def __repr__(self): # output that is less user-friendly than __str__(). More for debug purpurse for devs. __str__() has precedence
        return f"Ingredient(name={self.name}, amount={self.amount})"


if __name__ == '__main__':
    c = Ingredient("carrot", 5)
    p = Ingredient("pea", 4)
    a = Ingredient("apple", 1)
    s = c + p + a
    print(s)
