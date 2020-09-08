def rotate(array, ops):
    i = 0
    while i < ops:
        i += 1
        temp = array[0]
        array.pop(0)
        array.append(temp)
    for i in array:
        print(i, end=" ")


size, rotations = [int(i) for i in input().split()]
numbers = [int(i) for i in input().split()]
rotate(numbers, rotations)
