#!C:\Users\korch\AppData\Local\Programs\Python\Python312
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5


def replace_element(some_list, ind, new_value):
    if ind < 0 or ind > len(some_list):
        print(some_list)
    else:
        list_copy = some_list.copy()
        list_copy[ind] = new_value
        print("Copy:        ", list_copy)
        print("Original:    ", some_list)


replace_element(list_, index, element_to_replace)
