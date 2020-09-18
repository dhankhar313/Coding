str1 = input()
l3 = str1.split()
l2 = []
i = 0
while i < len(l3):
    for temp in l3[i]:
        l2.append(temp)
    i += 1
# print(l2)
for i in l2:
    if i.isalpha():
        continue
    else:
        l2.remove(i)
# print(l2)
str1 = "".join(l2)
l = len(str1)
l1 = []
if l > 2:
    if l == 3:
        str2 = str1[0:3]
        # str3 = str1[l]
        # l1.append(str2)
        # l1.append(str3)
        print(str2)
    else:
        str2 = str1[0:2]
        str3 = str1[l - 2:l]
        l1.append(str2)
        l1.append(str3)
        print("".join(l1), end="")
else:
    str2 = ""
    print(str2, end="")
