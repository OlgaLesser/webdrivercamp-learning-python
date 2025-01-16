#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def only_unique(lst):
    new_list = []
    sum_of_elements = 0
    for element in lst:
        if element not in new_list:
            new_list.append(element)
            sum_of_elements += element
    return sum_of_elements


if __name__ == "__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
