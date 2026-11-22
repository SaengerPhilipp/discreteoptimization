import numpy as np
from utils import solve_upper_triangular_squared
from GaussionElimination import gaussian_elimination_two_matrices_one_invertible

#start the calculation of a lattice basis of A in case gaussian elimination was first performed on A
def lattice_basis_gaussian_performed(A):
    indices = indices_of_invertible_submatrix(A)
    not_indices = np.delete(range(0,A.shape[1]),indices)
    B = A[:,indices]
    C = A[:,not_indices]
    return lattice_basis_inner(B,C)

def lattice_basis_inner(B,C):
    for i in range(C.shape[1]):
        #TODO not every B entered in this function has been through Gaussian elimination
        x = solve_upper_triangular_squared(B,C[:,i])
        for j in range(len(x)):
            if not x[j].is_integer():
                x_rounded = np.rint(x).astype(int)
                c_prime = C[:,i] - (B @ x_rounded)
                C[:,i] = B[:,j]
                B[:,j] = c_prime
                print(B)
                print(C)
                B[j:B.shape[0],j:B.shape[1]], C[j:C.shape[0],:] = gaussian_elimination_two_matrices_one_invertible(B[j:B.shape[0],j:B.shape[1]], C[j:C.shape[0],:])
                print(B)
                print(C)
                return lattice_basis_inner(B, C)
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

'''A = np.array([[1,2,3,4,5],[0,0,6,7,8],[0,0,0,0,8]])
idx = [1,2,3]
print(A)
print(A.shape[1],A.shape[0])
print(len(A[0]),len(A))
a = lattice_basis_gaussian_performed(A)'''

B = np.array([[2,6],[0,-10]])
C = np.array([[11],[-14]])
D = lattice_basis_inner(B,C)
print(D)