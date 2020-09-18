l1 = [int(i) for i in input().split()]
mat = [l1]
for i in range(1, len(l1)):
    l2 = []
    l2 = [int(i) for i in input().split()]
    mat.append(l2)
for i in range(len(l1)):
    for j in range(len(l1)):
        if j == len(l1) - 1:
            print(mat[i][j], end="\n")
        else:
            print(mat[i][j], end=" ")

for i in range(len(l1)):
    for j in range(len(l1)):
