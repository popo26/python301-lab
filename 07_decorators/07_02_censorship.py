# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


def censor(initial_func):
    def wrapper(msg):
        if "Shoot" in msg:
            new_msg = msg.replace("Shoot", "S****")
        return initial_func(new_msg)
    return wrapper

@censor
def message_func(msg):
    print(msg)

message_func("I bumped my toe! Shoot!")