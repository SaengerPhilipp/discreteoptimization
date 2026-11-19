import numpy as np
from GaussionElimination import gaussion_elimination

def diophantine_equations_solver(A,b):
    A,b = gaussion_elimination(A,b)
    