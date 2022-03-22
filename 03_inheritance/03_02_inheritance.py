# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

class Movie():
    def __init__(self, year, title) -> None:
        self.year = year
        self.title = title

    def __str__(self):
        return f"a movie called \"{self.title}\" was born in {self.year}"

class RomCom(Movie):
    def ticket(self):
        return "Ticket price is $10. For couple, $15. Find someone!"

class ActionMovie(Movie):
    def __init__(self, year, title) -> None:
        super().__init__(year, title)
        self.pg = "13"

    def __str__(self):
        return f"a movie called \"{self.title}\" was born in {self.year}. This is PG-{self.pg}."

movie = Movie(2000, "Happy Friday")
print(movie)

action_movie = ActionMovie(1958, "Super Action")
print(action_movie)

rom_com = RomCom(2020, "Super Sweet")
print(rom_com)
print(rom_com.ticket())

