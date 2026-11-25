import numpy as np
from utils import solve_upper_triangular_squared
from GaussionElimination import gaussian_elimination_two_matrices_one_invertible,gaussian_elimination_just_one_matrix

#start the calculation of a lattice basis of A
def lattice_basis(A):
    A_gaussian = gaussian_elimination_just_one_matrix(A.copy())
    print(A_gaussian)
    indices = indices_of_invertible_submatrix(A_gaussian)
    not_indices = np.delete(range(0, A.shape[1]), indices)
    B = A[:, indices]
    print(B)
    C = A[:, not_indices]
    B_gaussian = A_gaussian[:, indices]
    C_gaussian = A_gaussian[:, not_indices]
    return lattice_basis_inner(B,C,B_gaussian,C_gaussian)

#start the calculation of a lattice basis of A in case gaussian elimination was first performed on A
def lattice_basis_gaussian_performed(A):
    indices = indices_of_invertible_submatrix(A)
    not_indices = np.delete(range(0,A.shape[1]),indices)
    B = A[:,indices]
    C = A[:,not_indices]
    return lattice_basis_inner(B,C,B,C)

def lattice_basis_inner(B,C,B_gaussian,C_gaussian):
    for i in range(C.shape[1]):
        x = solve_upper_triangular_squared(B_gaussian,C_gaussian[:,i])
        for j in range(len(x)):
            if not x[j].is_integer():
                x_rounded = np.rint(x).astype(int)
                c_prime = C[:,i] - (B @ x_rounded)
                C[:,i] = B[:,j]
                B[:,j] = c_prime
                #OPTIMIZE this works but is maybe not optimal look in using LR partitioning as a way of calculating the inverse operation of the unimodular matrix from gaussian elimination
                B_new_gaussian, C_new_gaussian = gaussian_elimination_two_matrices_one_invertible(B,C)
                return lattice_basis_inner(B, C,B_new_gaussian,C_new_gaussian)
    return B

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