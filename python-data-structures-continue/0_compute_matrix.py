#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def compute_matrix(matrix=None):
    if matrix is None:
        matrix = []
    new_matrix = [list(map(lambda x: x**2, row)) for row in matrix]
    return new_matrix


if __name__ == "__main__":
    my_matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    modified_matrix = compute_matrix(my_matrix)
    print(f"Original: {my_matrix}")
    print(f"Modified: {modified_matrix}")
