#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def list_int_print(lst, i=0):
    count_el = 0
    for x in range(i):
        try:
            print(f"{lst[x]:d}", end='')
            count_el += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return count_el


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7]
    count = list_int_print(list_, 4)
    print(f"Count: {count:d}")
    list_ = [1, 2, "Camp", 5, [3, 4]]
    count = list_int_print(list_, len(list_))
    print(f"Count: {count:d}")
    count = list_int_print(list_, len(list_) + 2)
    print(f"Count: {count:d}")
