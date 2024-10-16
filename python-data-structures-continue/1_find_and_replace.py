#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def find_replace(original, find, replace):
    new_lst = []
    for item in original:
        if item == find:
            new_lst.append(replace)
        else:
            new_lst.append(item)
    return new_lst


if __name__ == "__main__":
    original_list = [0, 11, 13, 9, 4, 3, 4, 7, 7, 1, 0, 9]
    modified = find_replace(original_list, 9, 13)
    print(f"Original: {original_list}")
    print(f"Modified: {modified}")
