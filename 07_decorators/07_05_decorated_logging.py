# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import timeit

def time_it(function):
    def wrapper():
        time = timeit.timeit()
        print(f"To run this function, it took: {time} sec.")
        return function()
    return wrapper


@time_it
def message():
    print("Hello")

@time_it
def add():
    total = 0
    for n in range(0, 100000):
        total += n
    print(total)

message()
add()

