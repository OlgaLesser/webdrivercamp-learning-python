#!C:\Users\korch\AppData\Local\Programs\Python\Python312
def divide_safe(x, y):
    div_result = int()
    try:
        div_result = x/y
    except ZeroDivisionError:
        div_result = None
    finally:
        print("Result: ", div_result)
    return div_result


if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
