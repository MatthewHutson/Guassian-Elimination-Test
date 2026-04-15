# -- Imports -- #
import numpy as np
import copy
from typing import Callable, Any
import elelemtary_row_operations as ero
from utils import *
        
# -- Subroutines -- #
@enforce_types
def make_identity(size: int) -> np.ndarray:
    # -- Generates The Identity Matrix Of A Given Size -- #
    input: str = ""

    for i in range(size):
        for j in range(size):
            value: str = "1.0 " if i == j else "0.0 "
            input += value
        input += ";" 

    output: str = input[:-2]
    I: np.array = np.matrix(output)
    
    return I
          
@positive_int
def int_input(inputString: str) -> int: return input(inputString)

@enforce_types
def user_matrix(size: int) -> np.ndarray:
    # -- Creates A Matrix Of A Given Size To Represent The Equations -- #
    output: list[list[int]] = []
    
    for i in range(size):
        temp: list[int] = []
        for j in range(size):
            inputStr: str = "\nInput the value at (" + str(j + 1) + ", " +  str(i + 1) + "): "
            invalid: bool = True
            while invalid:
                try:
                    value: int = input(inputStr)
                    temp.append(float(value))
                    invalid = False
                except ValueError:
                    printLine("Input a real number!")

        output.append(temp)

    matrix: np.ndarray = np.array(output)
    
    return matrix

@enforce_types
def equality(matrix_1: np.ndarray, matrix_2: np.ndarray) -> bool:
    is_equal: bool = True

    for i, row in enumerate(matrix_1):
        for j, item in enumerate(row):
            is_equal = is_equal and float(item) == float(matrix_2[i, j])

    return is_equal

def find_inverse(matrix: np.ndarray) -> bool | np.ndarray:
    # -- Matrix Variables -- #
    size = len(matrix)
    identity: np.ndarray = make_identity(size)
    inverse: np.ndarray = copy.deepcopy(identity)
    working: np.array = copy.deepcopy(matrix)
    solveable: bool = True

    # -- Solution -- #
    for i in range(size):
        # -- Establishing A Non-Zero Diagonal -- #
        if working[i, i] == 0:
            j: int = size
            while working[j, i] == 0:
                j -= 1
                if j == 0: break

            if j == 0:
                # -- Column of 0's Found -- #
                solveable = False
                break

            elif j < size:
                # -- To Ensure That The Previous Non-Zero Is Preserved, We use Row Addition -- #
                ero.row_arithmetic(working, i, j, 1, i)
                ero.row_arithmetic(inverse, i, j, 1, i)
            else:
                # -- Swaps A Non-Zero With The Zero If We Don't Need Any Particular Value Yet -- #
                ero.swap_rows(working, i, j)
                ero.swap_rows(inverse, i, j)

    # -- Now That We Know That The Matrix Is Invertible -- #
    if solveable:
        for i in range(size):
            for j in range(0, size):
                # -- Scaling A Row So That Diagonal Value Is 1 -- #
                if j == i:
                    scale_factor = 1 / working[i, i]
                    ero.scale_row(working, i, scale_factor)
                    ero.scale_row(inverse, i, scale_factor)

                elif working[j, i] != 0:
                    # -- Getting The Non-Diagonal Items To 0 -- #
                    common_factor = working[i, i] / working[j, i]
                    ero.row_arithmetic(working, j, i, -1 * common_factor, j)
                    ero.row_arithmetic(inverse, j, i, -1 * common_factor, j)

            if equality(working, identity):
                break

    if solveable:
        return solveable, inverse
    else:
        return solveable, None


# -- Main -- #
@enforce_types
def main() -> None:
    # -- Matrix Variables -- #
    size: int = int_input("\nInput the size of the matrix: ")
    matrix: np.ndarray = user_matrix(size)
    invertible, inverse = find_inverse(matrix)

    if invertible:
        print("\nThe Inverse of\n\n", matrix, "\n\nis\n\n", inverse)
    else:
        printLine("\nThe matrix\n\n", matrix, "\n\nHas No Inverse!")

if __name__ == "__main__":
    main()