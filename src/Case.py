def is_pascal_case(word):
    found = False
    counter = 1
    if len(word) > 1:
        if word[0].islower():
            while not found and counter < len(word):
                if word[counter].isupper():
                    found = True
                counter += 1
    return found

def is_snake_case(word):
    found = False
    counter = 1
    if len(word) > 1:
        if word[0].islower():
            while not found and counter < len(word):
                if word[counter] == "-":
                    found = True
                counter += 1
    return found