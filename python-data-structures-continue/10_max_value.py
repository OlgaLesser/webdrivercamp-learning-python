#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def max_value(d):
    max_number = 0
    key = None
    if d is not None:
        for every_key in d:
            if d[every_key] > max_number:
                max_number = d[every_key]
                key = every_key
    return key


if __name__ == "__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")
    max_key = max_value(None)
    print(f"Max number - {max_key}")
