x, y = [int(i) for i in input().split()]
primes = []
for i in range(x, y):
    count1 = 0
    count2 = 0
    for j in range(2, int(i)):
        count1 += 1
        if i % j != 0:
            count2 += 1
    if count1 == count2:
        primes.append(str(i))
# print(primes)
primes2 = primes.copy()
primes3 = []
for i in primes:
    for j in primes2:
        if int(i) != int(j):
            primes3.append(int(i + j))
# print(primes3)
primes3 = list(dict.fromkeys(primes3))
primes4 = []
for i in primes3:
    count1 = 0
    count2 = 0
    for j in range(2, int(i)):
        count1 += 1
        if i % j != 0:
            count2 += 1
    if count1 == count2:
        primes4.append(i)
primes4.sort()
# print(primes4)
first = primes4[0]
last = primes4[-1]
# print(first, last)
reps = len(primes4)
# print(reps)
series = [first + last]
for i in range(reps):
    val = first + last
    first = last
    last = val
    series.append(last)
print(series[-3], end="")
