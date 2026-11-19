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

def solve_upper_triangular(A,b):
    x = [b[-1]/A[-1][-1]]
    for i in range(len(A)-2,-1,0):
        x = np.insert(x,0,A[i,i:len(A[0])])