l = input().split(',')
l.sort()
count = 0
for i in l:
    count += 1
    print(i, end=",") if count != len(l) else print(i, end="")
