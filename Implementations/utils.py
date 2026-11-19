import numpy as np

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

def solve_upper_triangular_squared(A,b):
    x = [b[-1]/A[-1][-1]]
    for i in range(len(A)-2,-1,-1):
        x = np.insert(x,0,(b[i]-np.inner(A[i, i+1:len(A[0])],x))/A[i][i])