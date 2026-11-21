import numpy as np

def lattice_basis_gaussian_performed(A):
    indices = indices_of_invertible_submatrix(A)
    B = A[:,indices]
    

def indices_of_invertible_submatrix(A):
    indices = []
    buffer = 0
    for i in range(len(A)):
        for j in range(i+buffer, len(A[0])):
            if A[i][j] != 0:
                indices.append(j)
                buffer+=j-i
                break
    return indices