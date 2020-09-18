def jumps(temp):
    index = clouds - 1
    steps = 0
    while index > 1:
        if temp[index - 2] == 0:
            steps += 1
            index -= 2
        elif temp[index - 1] == 0:
            steps += 1
            index -= 1
    if index != 0:
        steps += 1
    return steps


clouds = int(input())
l1 = [int(i) for i in input().split()]
print(jumps(l1))
