def ops(num):
    if num < 38:
        return num
    else:
        if num % 5 == 3 or num % 5 == 4:
            return num + (5 - (num % 5))
        else:
            return num


x = int(input())
l = [int(input()) for i in range(x)]
for j in l:
    print(ops(j))
