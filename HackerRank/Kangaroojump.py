k1, s1, k2, s2 = [int(i) for i in input().split()]
if k1 > k2 and s1 > s2:
    print("NO")
elif k2 > k1 and s2 > s1:
    print("NO")
else:
    kk1 = []
    kk2 = []
    for i in range(10):
        