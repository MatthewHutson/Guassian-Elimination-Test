# -- Imports -- #
import numpy as np
import copy
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
            inputStr: str = "Input the value at (" + str(j) + ", " +  str(i) + "): "
            invalid: bool = True
            while invalid:
                try:
                    value: int = input(inputStr)
                    temp.append(float(value))
                    invalid = False
                except ValueError:
                    printLine("Input a real number!")

        output.append(temp)

    matrix: np.ndarray = np.ndarray(output)
    
    return matrix

# -- Main -- #
@enforce_types
def main() -> None:
    size: int = int_input("Input the size of the matrix: ")
    identity: np.ndarray = make_identity(size)
    inverse: np.ndarray = copy.deepcopy(identity)
    #matrix: np.ndarray = user_matrix(size)
    #augmented_matrix: list[np.ndarray] = [matrix, inverse]


if __name__ == "__main__":
    main()