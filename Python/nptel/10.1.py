num = input()
l1 = [i for i in num]
n1 = 0
n0 = 0
for i in l1:
    if int(i) == 1:
        n1 += 1
        # print("n1=", n1)
    elif int(i) == 0:
        n0 += 1
        # print("n0=", n0)
    else:
        pass
if n1 == 1 or n0 == 1:
    print("YES", end="")
else:
    print("NO", end="")
