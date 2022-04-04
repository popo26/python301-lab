# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".



def censor(*args):
    def decorator_func(initial_func):
        def wrapper(msg):
            msg_lower = msg.lower()
            for word in args:
                if word in msg_lower:
                    word_list = []
                    for char in word[1:]:
                        new_char = char.replace(char, "*")
                        word_list.append(new_char)
                    word_list.insert(0, word[0])
                    revised_word = " ".join(word_list)
                    if word in msg:
                        new_msg = msg_lower.capitalize().replace(word, revised_word)      
                    elif word.capitalize() in msg:
                        new_msg = msg_lower.capitalize().replace(word, revised_word.capitalize()) 
            return initial_func(new_msg)
        return wrapper
    return decorator_func

@censor("shoot", "crab", "apple")
def message_func(msg):
    print(msg)

message_func("I saw a crab in the house")
message_func("I bumped my toes! Shoot!")
message_func("An apple is yummy")

