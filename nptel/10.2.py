str = input().split()
l1 = [int(i) for i in str]
# print(l1)
l1.sort()
# print(l1)
num = 1
# print(l1[-1])
while num < int(l1[-1]):
    if num in l1:
        num += 1
    if num not in l1:
        print(num, end="")
        num += 1
