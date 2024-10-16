#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def divide_list_safe(list1, list2, list_len):
    result = 0
    new_list = [0] * list_len
    for i in range(list_len):
        try:
            result = list1[i]/list2[i]
            new_list[i] = result
        except TypeError:
            new_list[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            new_list[i] = 0
            print("division by 0")
        except IndexError:
            new_list[i] = 0
            print("out of range")
    return new_list


if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()
    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
