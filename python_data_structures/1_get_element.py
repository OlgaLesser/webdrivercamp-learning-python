#!C:\Users\korch\AppData\Local\Programs\Python\Python312
list_ = [5, 4, 3, 2, 1]
index = 2


def get_element(lst, ind):
    if ind < 0:
        print(None)
    elif ind > len(lst):
        print(None)
    else:
        print("The element retrieved is", ind)


get_element(list_, index)
