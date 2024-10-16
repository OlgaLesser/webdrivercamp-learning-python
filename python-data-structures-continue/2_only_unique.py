#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def only_unique(list_=[]):
    sum = 0
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
            sum += i
    return sum


if __name__ == "__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
