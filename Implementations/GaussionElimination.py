import numpy as np

def gaussion_elimination(A,b):
    Ab = np.column_stack((A,b))
    gaussion_elimination_inner(Ab)
    return Ab

def gaussion_elimination_inner(A):
    print(A)
    if len(A)>1:
        for i in range(1,len(A)):
            f = A[i][0]
            A[i][0] = 0
            for j in range(1,len(A[i])):
                A[i][j] = A[i][j]*A[0][0] - A[0][j]*f
        gaussion_elimination_inner(A[1:len(A), 1:len(A[0])])