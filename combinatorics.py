import itertools

distinct = set()
for c in itertools.permutations("ball", 4):
    distinct.add(c)
print("ex3", len(distinct))

divisible = 0
for i in range(1, 300 + 1):
    for divisor in (3, 5, 7):
        if i % divisor == 0:
            divisible += 1
            break
print("ex4", divisible)