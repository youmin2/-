#32p
a = [38, 21, 53, 62, 19]
smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print(smallest)

#33p 
a = [38, 21, 53, 62, 19]
largest = a[0]

for i in a:
    if i > largest:
        largest = i

print(largest)

#34p
a = [38, 21, 53, 62, 19]
a.sort()

print(a[0], " and ", a[-1])

#35p
a = [38, 21, 53, 62, 19]
min_value = min(a)
max_value = max(a)

print(min_value, " and ", max_value)

#36p-1
a = [38, 21, 53, 62, 19]
result = 0

for i in a:
    result += i

print(result)

#36p-2
a = [38, 21, 53, 62, 19]
result = sum(a)
print(result)

#37p
a = [i for i in range(10)]
b = list(i for i in range(10))

print(a)
print(b)

#38p
a = [i + 5 for i in range(10)]
b = list(i * 2 for i in range(10))

print(a)
print(b)

#39p
a = [i for i in range(10) if i % 2 == 0]
print(a)

#40p
a = [i + 5 for i in range(10) if i % 2 == 1]
print(a)

#41p
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

#42p
a = [i * j  for j in range(2, 10)
            for i in range(1, 10)]
print(a)

#43p
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

#44p
a = list(map(str, range(10)))
print(a)

#45p
a = list(map(int, input().split()))
print(a)

#46p
a = (38, 21, 53, 62, 19, 53)
b = a.index(53)
print(b)

#47p
a = (10, 20, 30, 15, 20, 40)
b = a.count(20)
print(b)

#48p
a = (38, 21, 52, 62, 19)
for i in a:
    print(i, end=' ')

#49p
a = tuple(i + 5 for i in range(10) if i % 2 == 1)
print(a)

#50p-1
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

#50p-2
a = (38, 21, 53, 62, 19)
print(min(a), max(a), sum(a))

#56p
a = [[10, 20], [30, 40], [50, 60]]
b = [[10, 20],
     [30, 40],
     [50, 60]]

print(a)
print(b)

#57p
a = [[10, 20],
     [30, 40],
     [50, 60]]

print(a[1][0])
print(a[0][1])

a[2][1] = 100
print(a)

#58p
a = [[10, 20],
     [30, 40],
     [50, 60]]

for x, y in a:
    print(x, y)

#59p
a = [[10, 20],
     [30, 40],
     [50, 60]]

for x in a:
    print(x)
    for y in x:
        print(y, end=' ')
    print()