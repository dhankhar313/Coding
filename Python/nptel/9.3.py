def rotate_matrix(mat):
    if not len(mat):
        return
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1
    while left < right and top < bottom:
        prev = mat[top + 1][left]
        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top += 1
        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
        right -= 1
        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left += 1
    return mat


l = []
a = int(input())
for i in range(a):
    l1 = [x for x in input().split()]
    l.append(l1)
rl = [rotate_matrix(l)]
for i in range(a - 1):
    print(" ".join(l[i]))
print(" ".join(l[a - 1]), end="")