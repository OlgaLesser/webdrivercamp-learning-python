#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def max_value(d):
    biggest_key = None
    biggest_value = 0
    if d is None:
        return None
    else:
        for key, value in d.items():
            if value > biggest_value:
                biggest_key = key
                biggest_value = value
        return biggest_key


if __name__ == "__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")
    max_key = max_value(None)
    print(f"Max number - {max_key}")
