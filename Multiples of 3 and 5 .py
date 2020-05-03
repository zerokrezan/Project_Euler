import collections

liste = []

for i in range(1, 1000):
    if i % 3 == 0:
        liste.append(i)

for j in range(1, 1000):
    if j % 5 == 0:
        liste.append(j)

values_twice = ([item for item, count in collections.Counter(liste).items() if count > 1])
# you can print values_twice to see which numbers are twice
x = 0

for l in liste:
    x+=l

y = 0

for w in values_twice:
    y+=w

print(x-y)
