#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def mult_values(d):
    new_dict = {}
    for each_key in d:
        new_dict[each_key] = d[each_key] * 2
    return new_dict


if __name__ == "__main__":
    dict_print = __import__('6_dict_print').dict_print
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    new_dict = mult_values(dict_)
    dict_print(new_dict)
