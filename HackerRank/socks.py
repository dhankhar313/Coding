import math

num = int(input())
socks = [int(i) for i in input().split()]
temp = list(dict.fromkeys(socks))
# print(temp)
pair = 0
for i in temp:
    c = socks.count(i)
    c = math.floor(c / 2)
    pair += c
print(pair)
