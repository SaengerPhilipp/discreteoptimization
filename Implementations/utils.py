import numpy as np

#determines greatest common divisor
def ggt(m,n):
    if m > n:
        p = m%n
        if p == 0:
            return n
        else:
            return ggt(n,p)
    else:
        p = n%m
        if p == 0:
            return m
        else:
            return ggt(m,p)

#solve a system of linear equations consisting of a square matrix that is in upper triangular shape and a vector
def solve_upper_triangular_squared(A,b):
    x = [b[-1]/A[-1][-1]]
    for i in range(A.shape[0]-2,-1,-1):
        x = np.insert(x,0,(b[i]-np.inner(A[i, i+1:A.shape[1]],x))/A[i][i])