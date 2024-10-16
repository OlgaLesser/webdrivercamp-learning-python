#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def int_print(value):
    try:
        print(f"{value:d}")
        return True
    except Exception:
        return False


if __name__ == "__main__":
    my_value = 42
    if not (int_print(my_value)):
        print(f"{my_value} is not an integer")
    my_value = -100
    if not (int_print(my_value)):
        print(f"{my_value} is not an integer")
    my_value = "Webdriver Camp"
    if not (int_print(my_value)):
        print(f"{my_value} is not an integer")
