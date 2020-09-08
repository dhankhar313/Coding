def hourglass(mat):
    sum = []
    for i in range(len(temp) - 2):
        for j in range(len(temp) - 2):
            sum.append(
                mat[i][j] + mat[i][j + 1] + mat[i][j + 2] + mat[i + 1][j + 1] + mat[i + 2][j] + mat[i + 2][j + 1] +
                mat[i + 2][j + 2])
    sum.sort()
    return sum[-1]


temp = [int(i) for i in input().split()]
matrix = [temp]
for j in range(len(temp) - 1):
    matrix.append([int(i) for i in input().split()])
print(hourglass(matrix))
