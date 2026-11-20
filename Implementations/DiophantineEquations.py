import numpy as np
from GaussionElimination import gaussian_elimination
from utils import solve_upper_triangular_squared

def diophantine_equations_solver(A,b):
    A,b = gaussian_elimination(A,b)
    A_squared = determine_square_matrix(A)
    x = solve_upper_triangular_squared(A_squared,b) #TODO not defined if b is longer than the hight of A_squared

def determine_square_matrix(A):
    if len(A) > len(A[0]):
        return A[0:len(A[0]), :]
    else:
        return A[:,0:len(A)]