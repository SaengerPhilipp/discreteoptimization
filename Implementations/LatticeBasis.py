import numpy as np

def lattice_basis_gaussian_performed(A):
    indices = indices_of_invertible_submatrix(A)
    B = A[:,indices]



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
print(A)
print(A.shape[1],A.shape[0])
print(len(A[0]),len(A))
lattice_basis_gaussian_performed(A)