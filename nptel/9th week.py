str1 = input(":").split()
i = 0
l1 = []
while i < len(str1):
    str2 = str1[i]
    for j in str2:
        if j == j.upper():
            x = j.lower()
            str2.replace(j, x)
        elif j == j.lower():
            x = j.upper()
            str2.replace(j, x)
        else:
            pass
    l1.append(str2)
    i += 1
print(str1)
print(l1)