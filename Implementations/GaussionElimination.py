import numpy as np

#starts gaussion elimination
def gaussion_elimination(A,b):
    Ab = np.column_stack((A,b))
    gaussion_elimination_inner(Ab)
    return Ab[0:len(Ab), 0:len(Ab[0])-1], Ab[:,len(Ab[0])-1]

#actually does the elimination od gaussian elimination recursively
def gaussion_elimination_inner(A):
    if len(A)>1 and len(A[0])>1:
        if A[0][0] != 0 or switch_zero_row(A):
            for i in range(1,len(A)):
                f = A[i][0]
                if f != 0:
                    A[i][0] = 0
                    for j in range(1,len(A[i])):
                        A[i][j] = A[i][j]*A[0][0] - A[0][j]*f
        gaussion_elimination_inner(A[1:len(A), 1:len(A[0])])

#if a row used for eliminating other rows in the gaussion elimination starts with a zero we try to switch it with a row that contains a value not zero and return True otherwise we return false if we can't find such a row
def switch_zero_row(A):
    for i in range(1,len(A)):
        if A[i][0] != 0:
            A[[0,i]] = A[[i,0]]
            return True
    return False