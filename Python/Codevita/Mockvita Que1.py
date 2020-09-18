num = int(input())
l1 = []
for i in range(num):
    l1.append(input())
# print(l1)
for k in l1:
    total = 0
    coins = 0
    for j in range(1, int(k)):
        total += j
        coins += 1
        if total >= int(k):
            print(coins)
            break