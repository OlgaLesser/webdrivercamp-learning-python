#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def tuple_return(lst):
    if len(lst) == 0:
        lst[0] = None
    my_tuple = (len(lst), lst[0])
    return my_tuple
