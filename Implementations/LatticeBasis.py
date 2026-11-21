import numpy as np
from utils import solve_upper_triangular_squared

#start the calculation of a lattice basis of A in case gaussian elimination was first performed on A
def lattice_basis_gaussian_performed(A):
    indices = indices_of_invertible_submatrix(A)
    not_indices = np.delete(range(0,A.shape[1]),indices)
    B = A[:,indices]
    C = A[:,not_indices]
    return lattice_basis_inner(B,C)

def lattice_basis_inner(B,C):
    true_basis = True
    for i in range(C.shape[1]):
        x = solve_upper_triangular_squared(B,C[:,i])
        if not all(x_i.is_integer() for x_i in x ):
            true_basis = False

    if true_basis:
        return B
    else:
        return lattice_basis_inner(B,C)

#calculates the indices of the columns of a matrix such that the submatrix defined by those columns is invertible in case gaussian elimination was previously performed on said matrix
def indices_of_invertible_submatrix(A):
    indices = []
    buffer = 0
    for i in range(A.shape[0]):
        for j in range(i+buffer, A.shape[1]):
            if A[i][j] != 0:
                indices.append(j)
                buffer+=j-i
                break
    return indices

A = np.array([[1,2,3,4,5],[0,0,6,7,8],[0,0,0,0,8]])
idx = [1,2,3]
print(A)
print(A.shape[1],A.shape[0])
print(len(A[0]),len(A))
a = lattice_basis_gaussian_performed(A)