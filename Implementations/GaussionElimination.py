import numpy as np

def GaussionElimination(A,b):
    Ab = np.column_stack((A,b))
    for i in range(len(Ab)):
        print(1)

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

b = np.array([1,2,3])
GaussionElimination(A,b)
