import random as rd
import numpy as np

size = int(input())
matrix = []
for i in range(size):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)
print(matrix)
r = 0
c = 0
matrix = np.array(matrix)
while r != size and c != size:
    cost = 0
    if r != size - 1:
        r1 = rd.randint(r, r + 1)
    else:
        r1 = size - 1
    if r1 == r:
        c += 1
        r = r1
    else:
        r += 1
    cost += matrix[r][c]

