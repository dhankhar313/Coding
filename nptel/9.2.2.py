str1 = input()
l1 = str1.split()
l2 = []
l3 = []
i = 0
while i < len(l1):
    for temp in l1[i]:
        l2.append(temp)
    i += 1
print(l2)
for i in l2:
    if i.isalpha():
       continue
    else:
        l2.remove(i)
print(l2)
str1="".join(l2)