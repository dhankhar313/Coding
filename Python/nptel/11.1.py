l = [int(i) for i in input().split(',')]
count = 0
for i in l:
    count += 1
    num = ((100 * i) / 30) ** 0.5
    print(round(num), end=',') if count != len(l) else print(round(num), end='')
