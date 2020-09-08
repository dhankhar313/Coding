def sign(l1):
    ll, ul = [int(i) for i in l1]
    coords = [int(i) for i in range(ll, ul + 1)]
    print(coords)
    all_vals.append(coords)


num = int(input())
mid_vals = []
all_vals = []
all_vals2 = []
reps = {}
for i in range(num):
    temp = [int(i) for i in input().split()]
    mid_vals.append(temp)
for i in range(num):
    sign(mid_vals[i])
print("All:", all_vals)
for i in all_vals:
    for j in i:
        all_vals2.append(j)
print("All w/o lists:", all_vals2)
temp2 = list(dict.fromkeys(all_vals2))
print("No rep:", temp2)
for i in temp2:
    reps[str(i)] = all_vals2.count(i)
print(reps)
m = num
for i in temp2:
    while m > 0:
        if reps[str(i)] == m:
            print("1")
            print(i)
        m -= 1
