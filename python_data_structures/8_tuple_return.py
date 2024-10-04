#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def tuple_return(some_list):
    list_len = len(some_list)
    if list_len < 0:
        first_element = None
    else:
        first_element = some_list[0]

    new_list = [list_len, first_element]
    new_tuple = tuple(new_list)
    return new_tuple


my_list = [1, 2, 3, 4, 5]
result = tuple_return(my_list)
print(result)
print(f"List len = {result[0]}\nFirst element = {result[1]}")
