import numpy as np
import pandas as pd
m1=int(input("Enter the size of the row:"))
n1=int(input("Enter the size of the column:"))
mat1=[ [0 for _ in range(m1)] for _ in range(n1)]
for i in range(m1):
    for j in range(n1):
        e=int(input("Enter elements:"))
        mat1[i][j]=e
print(mat1)

m2=int(input("Enter the size of the row:"))
n2=int(input("Enter the size of the column:"))
mat2=[ [0 for _ in range(m2)] for _ in range(n2)]
for i in range(m2):
    for j in range(n2):
        e=int(input("Enter elements:"))
        mat2[i][j]=e
print(mat2)

#mat1=np.array([[1,2,3],[2,3,4],[21,3,4]])
#mat2=np.array([[2,7,9],[5,10,11],[31,22,11]])

def add(x,y):
    add=np.add(x,y)
    return add
def sub(x,y):
    sub=np.subtract(x,y)
    return sub
def mul(x,y):
    mul=np.multiply(x,y)
    return mul
def inv(x):
    inverse=np.linalg.inv(x)
    return inverse
def trans(x):
    transpose=transpose(x)
    return transpose
sol=add(mat1,mat2)
def det(x):
    deter=np.linalg.det(x)
    return deter

sol1=np.linalg.matrix_rank(mat1)
print(sol1)
sol2=np.linalg.eig(mat2)
print(sol2)
sol3=np.linalg.norm(mat2)
print(sol3)
np.trace(mat1)
np.min(mat1,axis=0)
    
        
