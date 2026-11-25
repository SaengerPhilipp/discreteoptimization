import numpy as np
from GaussionElimination import gaussian_elimination
from LatticeBasis import lattice_basis_gaussian_performed

def diophantine_equations_solver(A,b):
    A_gaussian,b_gaussian = gaussian_elimination(A,b)
    A_gaussian_cut_off = cut_off_zero_rows(A_gaussian)
    B = lattice_basis_gaussian_performed(A_gaussian_cut_off)

    #TODO first implement lattice basis with unimodular carry on then develop rest oft the algorithm

def cut_off_zero_rows(A):
    m = min(A.shape)
    for i in range(m-1,-1,-1):
        for j in range(A.shape[1]-1,i-1,-1):
            if A[i,j] != 0:
                return A[0:i+1,:]

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
B = cut_off_zero_rows(A)
print(B)