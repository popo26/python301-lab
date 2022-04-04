# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.


def decorator_func(initial_func):
    def wrapper_func(msg):
        print(f"\"{msg}\"")
        #return initial_func #With (), it doesn't work
    return wrapper_func

@decorator_func
def message_func(msg):
    print(msg)

message_func("Hello World!")




'''Without @ decorator'''

# def decorator_func(initial_func):
#     def wrapper_func():
#         print(f'"{initial_func}"')
#         return initial_func #With (), it doesn't work.
#     return wrapper_func

# decorated_message_func = decorator_func("Hello World!")
# decorated_message_func()