#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def list_int_print(lst, i=0):
    number_of_integers = 0
    for index in range(i):
        try:
            if isinstance(lst[index], int):
                print(f"{lst[index]:d}", end="")
                number_of_integers += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return number_of_integers


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]
    count = list_int_print(list_, 4)
    print(f"Count: {count:d}")
    list_ = [1, 2, "Camp", 5, [3, 4]]
    count = list_int_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_int_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
