#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def dict_update(my_dict, key, value):
    my_dict[key] = value
    return my_dict


if __name__ == "__main__":
    dict_print = __import__('6_dict_print').dict_print
    dict_ = {"libs": (1, 2, 3), "x": "Selenium", "lang": ["Java"], "frame": "Behave", "set": set()}
    new_dict = dict_update(dict_, 'lang', "Python")
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)
    new_dict = dict_update(dict_, 'stars', 5)
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)
