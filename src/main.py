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
            inputStr: str = "\nInput the value at (" + str(j) + ", " +  str(i) + "): "
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
            is_equal = is_equal and item == matrix_2[i][j]

    return is_equal

# -- Main -- #
@enforce_types
def main() -> None:
    # -- Matrix Variables -- #
    size: int = int_input("\nInput the size of the matrix: ")
    solved: bool = False
    identity: np.ndarray = make_identity(size)
    inverse: np.ndarray = copy.deepcopy(identity)
    initial: np.ndarray = user_matrix(size)
    working: np.array = copy.deepcopy(initial)
    augmented_matrix: list[np.ndarray] = [working, inverse]

    # -- Solution Variables -- #
    current_index: int = 0

    # -- Solution Loop -- #
    while not solved:
        function: Callable = None
        args: list[Any] = []

        current_row: np.ndarray = working[current_index] # -- Trying To Resolve 1 Row At A Time -- #

        try:
            for matrix in augmented_matrix: function(matrix, *args)
        except:
            # -- Function = None If Inverse Is Impossible -- #
            printLine("Matrix Has No Inverse!")
            quit()

        solved = equality(working, identity)

    print("The Inverse of", initial, "is", inverse)

if __name__ == "__main__":
    main()