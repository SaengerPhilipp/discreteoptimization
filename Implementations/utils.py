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
    x = np.zeros(len(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(x)