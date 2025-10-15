#3p-1
sting_var = 'Hello, world!'
print(sting_var.replace('world', 'Python'))
print(sting_var)

#3p-2
sting_var = 'Hello, world!'
sting_var = sting_var.replace('world', 'Python')
print(sting_var)

#4p
table = str.maketrans("aeiou", "12345")
print('apple'.translate(table))

#5p-1
sting_var = 'apple pear grape pineapple orange'
sting_var = sting_var.split()
print(sting_var)

#5p-2
sting_var = 'apple. pear, grape, pineapple, orange'
sting_var = sting_var.split(',')
print(sting_var)

#6p-1
sting_var = 'apple', 'pear', 'grape', 'pineapple', 'orange'
sting_var = " ".join(sting_var)
print(sting_var)

#6p-2
sting_var = 'apple', 'pear', 'grape', 'pineapple', 'orange'
sting_var = " - ".join(sting_var)
print(sting_var)

#7p-1
test_var = "ITcontents"
new_var = test_var.upper()
print(new_var)

#7p-2
test_var = "ITcontents"
new_var = test_var.lower()
print(new_var)

#8p
test_var = "ITcontents"
new_var1 = test_var.lstrip()
new_var2 = test_var.rstrip()
new_var3 = test_var.strip()
print('_' + test_var + '_')
print('_' + new_var1 + '_')
print('_' + new_var2 + '_')
print('_' + new_var3 + '_')

#9p 
test_var = "ITcontents"
new_var1 = test_var.lstrip(',.')
new_var2 = test_var.rstrip(',.')
new_var3 = test_var.strip(',.')
print('_' + test_var + '_')
print('_' + new_var1 + '_')
print('_' + new_var2 + '_')
print('_' + new_var3 + '_')

#10p
test_string = 'python'
new_string1 = test_string.ljust(10)
new_string2 = test_string.rjust(10)
print(new_string1)
print(new_string2)

#11p
test_string = 'python'
new_string1 = test_string.center(10)
new_string2 = test_string.center(11)
print(new_string1)
print(new_string2)

#12p
test_string = 'python'
new_string = test_string.rjust(10).upper()
print(new_string)

#13p
test_string1 = "35"
test_string2 = "3.14"
test_string3 = "Hello"

print(test_string1.zfill(4))
print(test_string2.zfill(6))
print(test_string3.zfill(10))
print(test_string3.zfill(5))

#14p
test_string1 = "apple pineapple banana"
search_index1 = test_string1.find('pl')
search_index2 = test_string1.find('zzz')

print(search_index1, search_index2)

#15p
test_string1 = "apple pineapple banana"
search_index1 = test_string1.rfind('pl')
search_index2 = test_string1.rfind('zzz')

print(search_index1, search_index2)

#16p
test_string1 = "apple pineapple banana"
search_index1 = test_string1.index('pl')
# search_index2 = test_string1.index('zzz')

print(search_index1)
#print(search_index2)

#17p-1
test_string1 = "apple pineapple banana"
search_index1 = test_string1.rindex('pl')

print(search_index1)

#17p-2
test_string1 = "apple pineapple banana"
search_cnt = test_string1.count('pl')

print(search_cnt)

#18p
name = "sukhyun"
score = 100

print("%s 성적은 %d점 입니다." % (name, score))

#19p
name = "sukhyun"
score = 99.99

print("%s 성적은 %5f점 입니다." % (name, score))

#20p
test_string = 'Python'

print("출력값: %10s" % test_string)
print("출력값: %-10s" % test_string)

#21p
test_string = "world!"
test_number = 100

print("Hello, {0}".format(test_string))
print("Hello, {0}".format(test_number))

#22p
test_string1 = "Python"
test_string2 = "score"
test_number1 = 100
test_number2 = 99

print("나의 이번학기 {0}과목의 {1}는 {3}점이 아닌 {2}점이다. 무조건 {2}."
      .format(test_string1, test_string2, test_number1, test_number2))

#23p
test_string1 = "Python"
test_string2 = "Script"
test_number1 = 3.6

print("Hello, {} {} {}".format(test_string1, test_string2, test_number1))

#24p
test_string1 = "Python"
test_number1 = 3.6

print("Hello, {version} {language}".format(language=test_string1, version=test_number1))

#25p
test_string = "Python"
print("{0:<10}".format(test_string))
print("{0:>10}".format(test_string))

#26p
test_string1 = "Python"
test_number1 = 3.6
new_text = f"Hello {test_number1} {test_string1}"

print(new_text)