ll, ul = input().split(',')
even = [int(i) for i in range(int(ll), int(ul) + 1, 2)]
# print(even)
j = 0
odd = [1, 3, 5, 7, 9]
for j in range(len(even)):
    temp = []
    for i in str(even[j]):
        temp.append(int(i))
    # print(temp)
    for x in temp:
        if x in odd:
            even.remove(even[j])
            even.insert(j, "Hy")
        else:
            pass
# print(even)
for m in range(len(even)):
    for k in even:
        if str(k).isalpha():
            even.remove(k)
# print(even)
count = 0
for i in even:
    count += 1
    print(i, end=",") if count != len(even) else print(i, end='')