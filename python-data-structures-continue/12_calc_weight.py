#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def calc_weight(some_list):
    if len(some_list) == 0:
        return 0
    else:
        numerator = sum(x * y for x, y in some_list)
        denominator = sum(y for x, y in some_list)
        return numerator / denominator


if __name__ == "__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
