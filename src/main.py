# -- Imports -- #
import numpy as np
import elelemtary_row_operations as ERO
from utils import *
        
# -- Subroutines -- #
@enforce_types
def make_identity(size: int) -> np.matrix:
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
def user_matrix(size: int) -> np.matrix:
    # -- Creates A Matrix Of A Given Size To Represent The Equations -- #
    input: str = ""
    inputStr: str = "Input the value at (" + str(j) + ", " +  str(i) + ")"

    for i in range(size):
        for j in range(size):
            invalid: bool = True
            while invalid:
                value: str = input(inputStr)
                try:
                    float(value)
                    string += str + " "
                    invalid = False
                except ValueError:
                    printLine("Input a real number!")

        input += ";" 

    output: str = input[:-2]
    matrix: np.array = np.matrix(output)
    
    return matrix

# -- Main -- #
@enforce_types
def main() -> None:
    size: int = int_input("Input the size of the matrix: ")
    Identity: np.matrix = make_identity(size)
    matrix: np.matrix = user_matrix(size)
    print(matrix)

if __name__ == "__main__":
    main()