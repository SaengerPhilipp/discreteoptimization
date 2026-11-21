import numpy as np

#starts gaussian elimination
def gaussian_elimination(A,b):
    Ab = np.column_stack((A,b))
    gaussian_elimination_inner(Ab)
    return Ab[:, 0:len(Ab[0])-1], Ab[:,len(Ab[0])-1]

#starts gaussian elimination and additionally returns the transforming unimodular matrix
def gaussian_elimination_unimodular(A,b):
    m = len(A)
    U = np.identity(m, dtype=int)
    Ab = np.column_stack((A,b,U))
    gaussian_elimination_inner_unimodular(Ab,m)
    return Ab[:, 0:len(Ab[0])-(1+m)], Ab[:,len(Ab[0])-(1+m)], Ab[:,len(Ab[0])-m:len(Ab[0])]

#actually does the gaussian elimination recursively
def gaussian_elimination_inner(A):
    if len(A)>1 and len(A[0])>1:
        if A[0][0] != 0 or switch_zero_row(A):
            gaussian_elimination_elimination(A)
            gaussian_elimination_inner(A[1:len(A), 1:len(A[0])])
        else:
            gaussian_elimination_inner(A[:,1:len(A[0])])

#actually does the gaussian elimination recursively and calculates the transforming unimodular matrix
def gaussian_elimination_inner_unimodular(A,m):
    if len(A)>1 and len(A[0])>m:
        if A[0][0] != 0 or switch_zero_row(A):
            gaussian_elimination_elimination(A)
            gaussian_elimination_inner_unimodular(A[1:len(A), 1:len(A[0])],m)
        else:
            gaussian_elimination_inner_unimodular(A[:,1:len(A[0])],m)

#does the elimination part
def gaussian_elimination_elimination(A):
    for i in range(1, len(A)):
        f = A[i][0]
        if f != 0:
            A[i][0] = 0
            for j in range(1, len(A[i])):
                A[i][j] = A[i][j] * A[0][0] - A[0][j] * f

#if a row used for eliminating other rows in the gaussian elimination starts with a zero we try to switch it with a row that contains a value not zero and return True otherwise we return false if we can't find such a row
def switch_zero_row(A):
    for i in range(1,len(A)):
        if A[i][0] != 0:
            A[[0,i]] = A[[i,0]]
            return True
    return False