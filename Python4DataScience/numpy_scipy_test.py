import numpy as np
import scipy.linalg

# a = np.arange(20,1,-3)
# b = [2,3,4,5]
# print(a)
# print(a[b])

# Z = np.array([92, 13, 44, 555, 1, -3])
# reversed_Z = np.flipud(Z)
# print(reversed_Z)
# print(reversed_Z[4])

# Z = np.arange(13, 1, -1)
# print(Z)
# for i in range(len(Z)):
#     if i % 3 == 0:
#         print(Z[i])

# y = np.arange(81).reshape(9,9)
# print(y)
# rows = [i for i in range(9) if i % 5 == 0]
# col = [1,3,4,5]
# print(y[[0], [1,3,4,5] ])
# print(y[[5], [1,3,4,5] ])

# z = np.arange(81, 6, -1).reshape(3,25)
# x = z[z<22]
# print(len(x))
# print(z)
# print(x)

# a = np.array([1, 1, 1, 1, 1], float)
# b = np.array([2, 2, 2, 2, 2], float)
# print(np.dot(a, b))

# A = np.array([[0, 9, 19, 13],[1, 20, 5, 13], [12,11,3,4]])
# B = np.array([[2,0,0,0],[1,2,2,0],[2,1,1,0],[0,0,1,1]])
# print(A@B)

# x = np.arange(5.4,2.1,-0.21)
# print(x)
# print(x.min())
# print(x.max())

# b = np.array([[-1, 33, 4, 1], [0, 1, 1, 0]])
# print(b.mean())

# x = np.arange(5).reshape((5,1))
# v = np.arange(5)
# print(x + v)

# A = np.array([[6, 0, 3], [0, -1, 2], [12, 3, 0]])
# lambdas, V = scipy.linalg.eig(A.T)
# # The linearly independent row vectors
# print(A[lambdas != 0,:])

# A = np.array([[1,-1,-1,0],[-1,2,-1,-1],[-1,-1,2,-1],[0,-1,-1,1]])
# # eigenvals, eigenvecs = scipy.linalg.eig(A)
# # print(eigenvals)

A = np.array([[2,4,0,4,1],[2,4,1,1,0],[1,1,1,2,2],[0,1,3,2,4],[2,2,2,0,2]])
A_rev = scipy.linalg.inv(A)
print(np.trace(A_rev))