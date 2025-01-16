#!/C:\Users\korch\AppData\Local\Programs\Python\Python312
def compute_matrix(some_matrix):
    squared_matrix = [list(map(lambda x: x**2, row)) for row in some_matrix]
    return squared_matrix


if __name__ == "__main__":
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    print(f"Original: {matrix}")
    print(f"Modified: {compute_matrix(matrix)}")
