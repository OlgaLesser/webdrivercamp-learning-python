#!C:\Users\korch\AppData\Local\Programs\Python\Python312
list_ = [5, 4, 3, 2, 1]
list2 = list_.copy()
index = 1
element_to_replace = 5


def replace_element(lst, ind, new_value):
    if 0 < ind < len(lst):
        lst[ind] = new_value
        print('Copy:    ', lst)
    else:
        print('Copy:    ', lst)


replace_element(list_, index, element_to_replace)
print('Original:', list2)
