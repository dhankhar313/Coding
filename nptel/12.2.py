str = input().split()
lc = 0
uc = 0
i = 0
while i < int(len(str)):
    for j in str[i]:
        if j.isalpha():
            if j == j.upper():
                uc += 1
            else:
                lc += 1
    i += 1
print(uc, lc, end="")
