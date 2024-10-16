#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def common_elements(a, b):
    my_list = []
    for each in a:
        if each in b:
            my_list.append(each)
    my_set = set(my_list)
    return my_set


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    same_element = common_elements(set_a, set_b)
    [print(x) for x in sorted(list(same_element))]
