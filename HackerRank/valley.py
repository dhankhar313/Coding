def countingvalleys(n, s):
    level = 0
    valleys = 0
    for c in s:
        prev = level
        level += 1 if c.upper() == 'U' else -1
        if prev == -1 and level == 0:
            valleys += 1
    print(valleys)


num = int(input())
str = input()
countingvalleys(num, str)
