import numpy as np

A = np.array([[1,-2,-1],[2,2,-1],[-1,-1,2]])
print("Matrix A: ", A)

B = np.array([6,1,1])
print("Matrix B: ", B)

Z = np.linalg.solve(A, B)
print("Final Matrix: ", Z)

# Matrix A:
# [
#  [ 1 -2 -1]
#  [ 2  2 -1]
#  [-1 -1  2]
# ]
# Matrix B: [6 1 1]
# Final Matrix: [ 3. -2.  1.]
