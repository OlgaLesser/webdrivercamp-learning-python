#!C:\Users\korch\AppData\Local\Programs\Python\Python312
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix(matr):
    for row in matr:
        for element in row:
            print(element, end=" ")
        print()


print_matrix(matrix)
