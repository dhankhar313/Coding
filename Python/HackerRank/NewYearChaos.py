def new_year(length, jumbled_array, list1):
    default_array = [int(k) for k in range(1, length + 1)]
    bribes = 0
    for j in default_array:
        if default_array.index(j) - jumbled_array.index(j) == 1:
            bribes += 1
        elif default_array.index(j) - jumbled_array.index(j) == 2:
            bribes += 2
        elif default_array.index(j) - jumbled_array.index(j) > 2:
            list1.append("Too chaotic")
            break
    list1.append(bribes)
    return list1


test = int(input())
bribes_list = []
for i in range(test):
    new_year(int(input()), [int(i) for i in input().split()], bribes_list)
for i in range(test):
    print(bribes_list[i])
