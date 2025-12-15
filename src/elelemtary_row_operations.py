# -- Imports -- #
import numpy as np
import copy
from utils import *

# -- Functions -- #
@enforce_types
def swap_rows(matrix: np.ndarray, index_1: int, index_2: int) -> None:
    # -- Swaps 2 Rows Of A Matrix -- #
    copy_matrix: np.ndarray = copy.deepcopy(matrix)
    row_1: np.ndarray = copy_matrix[index_1]
    row_2: np.ndarray = copy_matrix[index_2]

    matrix[index_1], matrix[index_2] = row_2, row_1

@enforce_types
def scale_row(matrix: np.ndarray, index: int, scalar: float) -> None:
    # -- Multiplies A Row By A Scalar -- #
    row: np.ndarray = matrix[index]
    row *= scalar

@enforce_types
def row_arithmetic(matrix: np.ndarray, index_1: int, index_2: int,  scalar: float = 1, out_index: int = None) -> None:
    # - Adding Or Subtracting A Scalar Multiple Of 1 Row From Another -- #
    copy_matrix: np.ndarray = copy.deepcopy(matrix)
    scale_row(copy_matrix, index_2, scalar)

    row_1: np.ndarray = copy_matrix[index_1]
    row_2: np.ndarray = copy_matrix[index_2]

    out_index = index_1 if out_index == None else out_index
    new_row: np.ndarray = row_1 + row_2

    matrix[out_index] = new_row
