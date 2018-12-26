
###########################
# Number Type Variables.. #
###########################

var1 = 1
var2 = 1.0
var3 = 1.2345
print(var1, var2, var3, sep="\n")

# 기본적인 사칙연산
print(1 + 2)
print(2 - 5)
print(4 * 5)
print(8 / 2)

# 나머지를 계산
print(10 % 3)
# 몫만 계산
print(10 // 3)
# 제곱 계산
print(2 **10)


###########################
# String Type Variables.. #
###########################

var1 = "A"
var2 = "Hello World"
var3 = ""
print(var1, var2, var3, sep="\n")

#표현해야 하는 문자의 형태에 따라 다른 출력방식을 사용할 수 있음.
print("Hello World?")
print('Hello "World?"')
print("Hello 'World?'")
print("""
Hello
World?
""")

#이스케이프 코드(\로 시작하는 특수한 타입의 문자)
print('Hello \'World?\'')
print("Hello \"Wotld?\"")
print('Hello \nWorld?')
print('Hello\tWorld?')
print('Hello \\World?\\')

# 문자열 데이터타입은 일부 연산자를 제공함.
str1 = "Hello"
str2 = " World"
print(str1 + str2) #Hello World

str1 = "ba"
str2 = "na"
print(str1 + str2 * 2) # ?

# 문자열은 내부적으로는 문자열의 길이만큼의 크기를 가지는 배열의 형태.
str1 = "KAKAO TOGETHER"
print(str1[0]) #0번째 인덱스
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[-1]) # 끝에서부터 역행하는 인덱스

# 긴 문자열을 자르기 위한 슬라이싱 기능을 제공함.
# str1 에서 TOGETHER 만 출력하고 싶다면?
print(str1[6:14]) #TOGETHER
# 변수명[시작 인덱스 이상:끝 인덱스미만] 
print(str1[6:])

# count, find, index, join, upper, lower, replace, sort, strip, isdigit 등의 내장 함수를 사용할 수 있음.

###########################
# List Type Variables..   #
###########################

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [1,"two",3,"four",5]
list4 = []

# 슬라이싱, 인덱싱, append, sort, reverse, index, insert, remove, count 등의 내장 함수를 사용할 수 있음.

###########################
# Tuple Type Variables..  #
###########################

tuple1 = (1,2,3,4)
tuple2 = ("one","two","three","four")
tuple3 = (1,"two",3,"four",5)
tuple4 = (1,)

# 리스트 형태와 비슷하지만, 데이터를 변경할 수 없음.



###############################
# Dictionary Type Variables.. #
###############################

dict1 = {'name' : 'hori', 'age' : 3, 'email' : 'geralt.rivia@kakaocorp.com'}
print(dict1['name'])
print(dict1['age'])
print(dict1['email'])
dict1['occupation'] = 'developer'
print(dict1['occupation'])

# keys, values, items, get 등의 내장함수를 사용할 수 있음.

