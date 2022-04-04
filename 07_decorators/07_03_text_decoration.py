# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
    def decorator_func(initial_func):
        def wrapper(msg):
            # symbol = "*"
            print(symbol * 20)
            print(msg)
            print(symbol * 20)
            
            # return initial_func(msg)
        return wrapper
    return decorator_func

@decorate("*")
def message(msg):
    print(msg)

message("Awesome")

