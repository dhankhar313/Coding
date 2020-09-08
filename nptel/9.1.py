str1 = input()
l1 = str1.split()
l2 = []
l3 = []
i = 0
while i < len(l1):
    for temp in l1[i]:
        l2.append(temp)
    l3.append(len(l1[i]))
    i += 1
for i in range(len(l2)):
    x = l2[i]
    if x.isalpha():
        if x == x.upper():
            l2[i] = x.lower()
        else:
            l2[i] = x.upper()
    else:
        pass
# print(l2, "\nLength: ", l3)
ll = 0
ul = 0
i = 0
l4 = []
for i in l3:
    ul += i
    temp2 = "".join(l2[ll:ul])
    l4.append(temp2)
    ll += i
# print(l4)
print(" ".join(l4), end="")