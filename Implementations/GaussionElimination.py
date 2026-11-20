import numpy as np

#starts gaussian elimination
def gaussian_elimination(A,b):
    Ab = np.column_stack((A,b))
    gaussian_elimination_inner(Ab)
    return Ab[:, 0:len(Ab[0])-1], Ab[:,len(Ab[0])-1]

def gaussian_elimination_unimodular(A,b):
    m = len(A)
    U = np.identity(m, dtype=int)
    Ab = np.column_stack((A,b,U))
    gaussian_elimination_inner_unimodular(Ab,m)
    print(Ab)
    return Ab[:, 0:len(Ab[0])-(1+m)], Ab[:,len(Ab[0])-(1+m)], Ab[:,len(Ab[0])-m:len(Ab[0])]

#actually does the elimination od gaussian elimination recursively
def gaussian_elimination_inner(A):
    if len(A)>1 and len(A[0])>1:
        if A[0][0] != 0 or switch_zero_row(A):
            for i in range(1,len(A)):
                f = A[i][0]
                if f != 0:
                    A[i][0] = 0
                    for j in range(1,len(A[i])):
                        A[i][j] = A[i][j]*A[0][0] - A[0][j]*f
            gaussian_elimination_inner(A[1:len(A), 1:len(A[0])])
        else:
            gaussian_elimination_inner(A[:,1:len(A[0])])

def gaussian_elimination_inner_unimodular(A,m):
    if len(A)>1 and len(A[0])>m:
        if A[0][0] != 0 or switch_zero_row(A):
            for i in range(1,len(A)):
                f = A[i][0]
                if f != 0:
                    A[i][0] = 0
                    for j in range(1,len(A[i])):
                        A[i][j] = A[i][j]*A[0][0] - A[0][j]*f
            gaussian_elimination_inner_unimodular(A[1:len(A), 1:len(A[0])],m)
        else:
            gaussian_elimination_inner_unimodular(A[:,1:len(A[0])],m)

#if a row used for eliminating other rows in the gaussian elimination starts with a zero we try to switch it with a row that contains a value not zero and return True otherwise we return false if we can't find such a row
def switch_zero_row(A):
    for i in range(1,len(A)):
        if A[i][0] != 0:
            A[[0,i]] = A[[i,0]]
            return True
    return False

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([10,11,12])

B,c,U=gaussian_elimination_unimodular(A,b)
D,e=gaussian_elimination(A,b)
print(B)
print(D)
print(U@A)
print(U)
print(c)
print(e)
