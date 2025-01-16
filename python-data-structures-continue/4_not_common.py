#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def not_common_elements(a, b):
    new_set = a.symmetric_difference(b)
    return new_set


if __name__ == "__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]
