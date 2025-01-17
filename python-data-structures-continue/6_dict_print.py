#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def dict_print(some_dict):
    for key in sorted(some_dict):
        print(f"{key}: {some_dict[key]}")


if __name__ == "__main__":
    dict_ = {"libs": (1, 2, 3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(dict_)
