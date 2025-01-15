#!C:\Users\korch\AppData\Local\Programs\Python\Python312
list_ = [5, 4, 3, 2, 1]
index = 2


def get_element(some_list, i):
    if i < 0 or i > len(some_list):
        return None
    else:
        print("The element retrieved is", some_list[i])


get_element(list_, index)
