# -- Imports -- #
import numpy as np
import typing as tp
from utils import *
        
# -- Subroutines -- #
@enforce_types
def makeIdentity(size: int) -> np.array:
    I: np.array = np.array([])

    for i in range(size):
        temp = []
        for j in range(size):
            value = 1 if i == j else 0
            temp.append(value)
        np.append(I, temp)
        temp = None
        value = None
    
    return I
          
@positive_int
@enforce_types
def intInput(inputString: str) -> int: return input(inputString)

# -- Main -- #
@enforce_types
def main() -> None:
    size: int = intInput("Input the size of the matrix: ")
    Identity: np.array = makeIdentity(size)
    print(Identity)

if __name__ == "__main__":
    main()