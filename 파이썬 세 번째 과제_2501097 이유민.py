#과제 11
a = list(map(int, input('숫자 5개를 입력하세요: ').split()))
print(a)

b = input('문자 1개를 입력하세요: ')
a.append(b)

print(a)

#과제 12
a = list(map(int, input('숫자 5개를 입력하세요: ').split()))
del a[-2:]

print(a)

#과제 13
a = list(map(int, input('숫자 5개를 입력하세요: ').split()))

for index, value in enumerate(a, start = 101):
    print(index, value)

#과제 14
a = [10, 20, 30, 40, 30, 20, 10]
b = a.count(20)

print(b)

#과제 15
a = list(map(int, input('숫자 10개를 입력하세요: ').split()))

m = min(a)
M = max(a)

print(m, M)

#과제 16
a = list(map(int, input('숫자 10개를 입력하세요: ').split()))

a.remove(min(a))
a.remove(max(a))

print(a)

#과제 17
a = [10, 20, 30, 40, 30, 20, 10]
a.remove(20)
a.remove(20)

print(a)

#과제 18
a = [i for i in range(1, 6)]

print(a)

#과제 19
a = [i for i in range(1, 21) if i % 2 != 0]

print(a)

#과제 20
a, b = map(int, input().split())

c = [2 ** i for i in range(a, b+1)]

del c[1]
del c[-2]

print(c)

#과제 21
a = input()
a = a.replace('Hello', 'Hi')

print(a)

#과제 22
a = input('4개의 문자를 입력하세요: ').split()
a = "/".join(a)

print(a)

#과제 23
a = input('본인의 성을 영어로 입력하세요: ')
a_lower = a.lower()

print("%10s" % a_lower)

#과제 24
a = list(map(int, input('물품 가격을 세미콜론을 붙여 입력하세요: ').split(';')))
a.sort(reverse=True)

for i in a:
    print("%9s" % i)