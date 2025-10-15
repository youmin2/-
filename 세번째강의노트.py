#2p-1
fruits = ("apple", 'orange', "grape")

for i in fruits:
    print(i)
    
#2p-2
test_string = "Python"

for i in test_string:
    print(i, end=" ")
    
#3p
test_string = "Python"

for i in reversed(test_string):
    print(i, end=" ")
    
#4p
test_var = tuple(range(-4, 10, 2))
print(test_var)

#4p 연습
a = tuple(range(5, 12))
print(a)

#5p
test_var = tuple(range(-4, 10, 2))

print(0 in test_var)
print(9 in test_var)

#6p
b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(b[4:7], b[4:])
print(b[:7:2], b[:-1])

#7p
r = range(10)

print(r[4:7], r[4:])
print(r[:7:2], r[:-1])

#8p
hello = 'Hello, world!'

print(hello[2:9])
print(hello[2:])
print(hello[:9:2])
print(hello[:-1])

#10p
a = [10, 20, 30]
a.append(500)

print(a, ",", len(a))

#11p-1
a = []
a.append(100)

print(a, ",", len(a))

#11p-2
a = [10, 20, 30]
a.append([500, 600])

print(a, ",", len(a))

#12p
a = [10, 20, 30]

a.extend([500, 600])
print(a, ",", len(a))

b = [10, 20, 30]
c = [500, 600]
d = a+c
print(d, ",", len(d))

#13p-1
a = [10, 20, 30]

a.insert(2, 500)
print(a, ",", len(a))

#13p-2
a = [10, 20, 30]

a.insert(100, 500)
print(a, ",", len(a))

#14p
a = [10, 20, 30]

a.insert(len(a), 500)
print(a, ",", len(a))

a.insert(1, [500, 600])
print(a, ",", len(a))

#a.insert(1, 500, 600)
#print(a, ",", len(a))

a[2:4] = 1000, 2000
print(a, ",", len(a))

#15p
a = [10, 20, 30]
b = a.pop()

print(a, ",", len(a))
print(b)

#16p-1
a = [10, 20, 30]
b = a.pop(1)

print(a, ",", len(a))
print(b)

#16p-2
a = [10, 20, 30]
#b = a.pop(1)
del a[1]

print(a, ",", len(a))

#17p-1
a = [10, 20, 30]
a.remove(20)

print(a, ",", len(a))

#17p-2
a = [10, 20, 30, 20]
a.remove(20)

print(a, ",", len(a))

#18p
a = [10, 20, 30, 15, 20, 40]
result = a.index(20)

print(result)

#19p
a = [10, 20, 30, 15, 20, 40]
result = a.count(20)

print(result)

#20p-1
a = [10, 20, 30, 15, 20, 40]
a.reverse()

print(a)

#20p-2
a = [10, 20, 30, 15, 20, 40]
a.sort(reverse=True)

print(a)

#21p-1
a = [10, 20, 30, 15, 20, 40]
a.clear()

print(a, ",", len(a))

#21p-2
a = [10, 20, 30, 15, 20, 40]
del a[:]

print(a, ",", len(a))

#22p
a = [10, 20, 30]
a[len(a):]= [500]

print(a, ",", len(a))

#23p
a = [10, 20, 30]
a[len(a):]= [50, 600]

print(a, ",", len(a))

#25p
a = [0, 0, 0, 0, 0]
b = a

b[2] = 99

print(a)

#26p
a = [0, 0, 0, 0, 0]
b = a.copy()

b[2] = 99

print(a, ",", b)

#27p-1
a = [38, 21, 53, 62, 19]

for i in a:
    print(i, end=' ')

#27p-2
a = [38, 21, 53, 62, 19]

for index, value in enumerate(a):
    print(index, value, end=' / ')

#28p
a = [38, 21, 53, 62, 19]

for index, value in enumerate(a):
    print(index + 1, value)

#29p
a = [38, 21, 53, 62, 19]

for index, value in enumerate(a, start = 1):
    print(index, value)

#30p
a = [38, 21, 53, 62, 19]

i = 0

while i < len(a):
    print(i)
    i += 1

#32p
a = [38, 21, 53, 62, 19]
smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print(smallest)

#61p-1
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][1] = 500

print(a)
print(b)

#61p-2
import copy 

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)
b[0][1] = 500

print(a)
print(b)