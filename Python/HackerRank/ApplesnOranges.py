h1, h2 = [int(i) for i in input().split()]
at, ot = [int(i) for i in input().split()]
na, no = [int(i) for i in input().split()]
apples = [int(i) + at for i in input().split()]
orange = [int(i) + ot for i in input().split()]
# print(apples, orange)
count1 = 0
count2 = 0
for i in apples:
    if h1 <= i <= h2:
        count1 += 1
for j in orange:
    if h1 <= j <= h2:
        count2 += 1
print(count1)
print(count2)
