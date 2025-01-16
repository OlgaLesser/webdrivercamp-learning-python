#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def common_elements(a, b):
    my_set = a.intersection(b)
    return my_set


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    same_element = common_elements(set_a, set_b)
    [print(x) for x in sorted(list(same_element))]
