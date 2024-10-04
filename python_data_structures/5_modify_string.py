#!C:\Users\korch\AppData\Local\Programs\Python\Python312
string = """AbraCadabra
A new string voila!"""


def remove_char(some_string):
    new_string = ""
    for char in some_string:
        if char.lower() != 'a':
            new_string += char
        elif char.upper() != 'A':
            new_string += char
    return new_string


print(remove_char(string))
