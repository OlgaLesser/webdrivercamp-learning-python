#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def map_list(list_=[], num=0):
    return list(map(lambda x: x * num, list_))


if __name__ == "__main__":
    my_list = [5, 4, 3, 2, 1, 7]
    new_list = map_list(my_list, 4)
    print(f"Original: {my_list}")
    print(f"Modified: {new_list}")
