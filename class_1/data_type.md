# 변수와 자료형.
<br/>

> ## 숫자형 변수(number type)
-  아래와 같이 선언할 수 있음
```
var1 = 1
var2 = 1.0
var3 = 1.2345
print(var1, var2, var3)
 ```
 - 사칙 연산이 가능하고, 몇 가지 추가적인 연산이 가능
```
print(1 + 2)
print(2 - 5)
print(4 * 5)
print(8 / 2)
print(10 % 3) #나머지를 계산합니다.
print(10 // 3) #몫만 계산합니다.
print(2 **10) #제곱을 계산합니다.
 ```
<br/>

> ## 문자열 형태 변수(string type)
- 아래와 같이 선언할 수 있음
```
var1 = "A"
var2 = "Hello World"
var3 = ""
print(var1, var2, var3)
```
- 제한적인 연산이 가능함
```
str1 = "Hello"
str2 = " World"
print(str1 + str2) #Hello World

str1 = "ba"	
str2 = "na"
print(str1 + str2 * 2) #banana
```

- 여러 가지 출력방식을 이용할 수 있음
```
print("Hello World?")
print('Hello "World?"')
print("Hello 'World?'")
print("""
Hello
World?
""")
```
- 이스케이프 코드(\로 시작하는 문자) 를 사용해, 특수문자, 줄넘김, 탭 등을 사용할 수 있음
```
print('Hello \'World?\'')
print("Hello \"Wotld?\"")
print('Hello \nWorld?')
print('Hello\tWorld?')
print('Hello \\World?\\')
```
<br/>

> ## 리스트 타입 변수(list type)
- 여러 개의 데이터를 하나의 변수에 저장하기 위한 용도
- 아래와 같이 선언할 수 있음

```
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [1,"two",3,"four",5]
list4 = []

list5 = list()
list6 = list(range(10))
list7 = list(range(0,10))

```
<br/>

> ## 튜플 타입 변수(tuple type)

- 리스트와 비슷하지만, 한 번 선언한 뒤에는 내용을 변경할 수 없음(읽기 전용 리스트)
- 리스트를 쓰면 안되나? 라고 생각할 수 있지만 필요할 때가 있음
- 아래와 같이 선언할 수 있음
```
tuple1 = (1,2,3,4)
tuple2 = ("one","two","three","four")
tuple3 = (1,"two",3,"four",5)
tuple4 = (1,)
```

> ## 시퀀스 자료형의 활용

- 리스트, 튜플, 문자열 형태는 데이터들이 연속적(sequential) 으로 이어져 있습니다.
![시퀀스 자료형의 개념](https://dojang.io/pluginfile.php/13491/mod_page/content/3/011001.png)


11.1 시퀀스 자료형의 공통 기능 사용하기 << 이 부분 정리가 필요함.

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