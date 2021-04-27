import numpy as np


def set_matrix_zeros(input_matrix: np.ndarray):
    """Set all of the rows and colums of elements that are zero. We need to do this in place."""
    num_rows, num_columns = input_matrix.shape
    all_zero_indexes = np.argwhere(input_matrix == 0)
    for zero_entry_index in all_zero_indexes:
        input_matrix[zero_entry_index[0], :] = np.zeros(num_columns)
        input_matrix[:, zero_entry_index[1]] = np.zeros(num_rows)


if __name__ == "__main__":
    input_matrix = np.array([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    set_matrix_zeros(input_matrix)
    assert np.allclose(input_matrix, np.array([[0,0,0,0],[0,4,5,0],[0,3,1,0]]))
