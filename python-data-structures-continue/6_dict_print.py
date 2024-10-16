#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def dict_print(dict_):
    my_list = sorted(list(dict_.keys()))
    for i in my_list:
        print(i, ": ", dict_[i])


if __name__ == "__main__":
    my_dict = {"libs": (1, 2, 3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(my_dict)
