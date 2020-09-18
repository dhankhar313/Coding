import itertools

low, high = [int(i) for i in input().split()]
reps = int(input())
perms = [' ' for i in itertools.product(range(low, high + 1), repeat=reps) if sum(i) % 2 == 0]
print(len(perms), end="")
