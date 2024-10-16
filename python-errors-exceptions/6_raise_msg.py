#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def raise_message(message=""):
    raise NameError(message)


if __name__ == "__main__":
    try:
        raise_message("I love Python!")
    except NameError as ne:
        print(ne)
