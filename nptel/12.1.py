num = int(input())
m = 0
l2 = []
l3 = []
while m < num:
    str = input().split()
    j = 0
    while j < len(str):
        l1 = []
        for i in str[j]:
            if i.isalpha():
                if i == i.upper():
                    l1.append(i)
                else:
                    l1.append(i.upper())
        l2.append("".join(l1))
        j += 1
    m += 1
    l3.append("".join(l2))
print(l3)
