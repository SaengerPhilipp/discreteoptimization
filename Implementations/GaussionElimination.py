import numpy as np

#gaussian elimination for Ax=b

#starts gaussian elimination
def gaussian_elimination(A,b):
    Ab = np.column_stack((A,b))
    gaussian_elimination_inner(Ab)
    return Ab[:, 0:A.shape[1]-1], Ab[:,A.shape[1]-1]

#starts gaussian elimination and additionally returns the transforming unimodular matrix
def gaussian_elimination_unimodular(A,b):
    m = A.shape[0]
    U = np.identity(m, dtype=int)
    Ab = np.column_stack((A,b,U))
    gaussian_elimination_inner_unimodular(Ab,m)
    return Ab[:, 0:A.shape[1]-(1+m)], Ab[:,A.shape[1]-(1+m)], Ab[:,A.shape[1]-m:A.shape[1]]

#gaussian elimination for AX=C

#starts gaussian elimination for AX = C with A invertible
def gaussian_elimination_two_matrices_one_invertible(A, C):
    AC = np.column_stack((A,C))
    gaussian_elimination_inner(AC)
    return AC[:,0:A.shape[1]], AC[:,A.shape[1]:AC.shape[1]]

#starts gaussian elimination for AX = C and constructs operates the inverse operations on a given matrix
def gaussian_elimination_two_matrices_one_invertible_track_inverse_unimodular(A,C,U):
    AC = np.column_stack((A,C))
    gaussian_elimination_inner_inverse_unimodular(AC,U)
    return AC[:,0:A.shape[1]], AC[:,A.shape[1]:AC.shape[1]]

#general gaussian elimination

#actually does the gaussian elimination recursively
def gaussian_elimination_inner(A):
    if A.shape[0]>1 and A.shape[1]>1:
        if A[0][0] != 0 or switch_zero_row(A):
            gaussian_elimination_elimination(A)
            gaussian_elimination_inner(A[1:A.shape[0], 1:A.shape[1]])
        else:
            gaussian_elimination_inner(A[:,1:A.shape[1]])

#actually does the gaussian elimination recursively and calculates the transforming unimodular matrix
def gaussian_elimination_inner_unimodular(A,m):
    if A.shape[0]>1 and A.shape[1]>m:
        if A[0][0] != 0 or switch_zero_row(A):
            gaussian_elimination_elimination(A)
            gaussian_elimination_inner_unimodular(A[1:A.shape[0], 1:A.shape[1]],m)
        else:
            gaussian_elimination_inner_unimodular(A[:,1:A.shape[1]],m)

#actually does the gaussian elimination recursively and calculates the inverse transforming unimodular
def gaussian_elimination_inner_inverse_unimodular(A,U):
    if A.shape[0]>1 and A.shape[1]>1:
        if A[0][0] != 0 or switch_zero_row(A):
            gaussian_elimination_elimination_inverse_unimodular(A,U)
            gaussian_elimination_inner(A[1:A.shape[0], 1:A.shape[1]])
            #TODO the recursion does not work properly yet
        else:
            gaussian_elimination_inner(A[:,1:A.shape[1]])

#does the elimination part
def gaussian_elimination_elimination(A):
    for i in range(1, A.shape[0]):
        f = A[i][0]
        if f != 0:
            A[i,:] = A[i]*A[0][0]- A[0]*f

def gaussian_elimination_elimination_inverse_unimodular(A,U):
    #TODO U does not get transformed jet
    for i in range(1, A.shape[0]):
        f = A[i][0]
        if f != 0:
            A[i][0] = 0
            for j in range(1, A.shape[1]):
                A[i][j] = A[i][j] * A[0][0] - A[0][j] * f

#if a row used for eliminating other rows in the gaussian elimination starts with a zero we try to switch it with a row that contains a value not zero and return True otherwise we return false if we can't find such a row
def switch_zero_row(A):
    for i in range(1,A.shape[0]):
        if A[i][0] != 0:
            A[[0,i]] = A[[i,0]]
            return True
    return False