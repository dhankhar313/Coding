import itertools

num = int(input())
num_list = [int(i) for i in input().split()]
count = 0
perms = []

max_len = len(str(bin(max(num_list))).replace("0b", ""))
for i in range(1, num + 1):
    temp = itertools.permutations(num_list, i)
    perms.append(temp)

final = []
for i in perms:
    for j in i:
        final.append(j)

final = set(map(lambda x: tuple(sorted(x)), final))

for i in final:
    t_zeros = 0
    t_ones = 0
    for m in i:
        bin1 = str(bin(m)).replace("0b", "")
        if len(bin1) < max_len:
            diff = max_len - len(bin1)
            free = ''
            for k in range(diff):
                free += '0'
            bin1 = free + bin1
        t_zeros += bin1.count('0')
        t_ones += bin1.count('1')
    if t_ones == t_zeros and t_ones != 0:
        count += 1

if len(str(count)) < max_len:
    count = str(bin(int(count)).replace("0b", ""))
    diff = max_len - len(count)
    free = ''
    for k in range(diff):
        free += '0'
    count = free + count
    print(count)
else:
    print(count)
