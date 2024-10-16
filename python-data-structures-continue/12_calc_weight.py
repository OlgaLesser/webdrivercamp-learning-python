#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def calc_weight(list_=[]):
    y = 0
    z = 0
    for i in list_:
        x = i[0] * i[1]
        y = y + x
        z = i[1] + z
    my_result = y / z
    return my_result


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
