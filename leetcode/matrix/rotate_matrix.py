import numpy as np


def rotate_square_matrix(input_matrix: np.ndarray):
    num_rows, num_columns = input_matrix.shape
    assert num_rows == num_columns, "We only support square matrices."
    rotated_matrix = np.zeros((num_rows, num_columns))
    for row_num in range(num_rows):
        for column_num in range(num_columns):
            rotated_matrix[row_num][column_num] = input_matrix[num_rows - column_num - 1][row_num]
    return rotated_matrix


if __name__ == "__main__":
    input_matrix = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
    assert np.allclose(rotate_square_matrix(input_matrix=input_matrix), np.array([[7, 4, 1], [8, 5, 2], [9, 6, 3]]))
