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

- 리스트, 튜플, 문자열 형태는 데이터들이 연속적(sequential) 으로 이어져 있음.  
![시퀀스 자료형의 개념](https://dojang.io/pluginfile.php/13491/mod_page/content/3/011001.png)


























-  시퀀스 자료형의 공통 기능 사용하기
   - 시퀸스 자료형은 공통된 동작과 기능을 제공함.

1. in(not in)

```
>>> a = [1,2,3,4,5]
>>> 3 in a
True

>>> 10 in a 
False

>>> 3 not in a
False

>>> 10 not in a
True

# tuple, range, string 에도 동잏하게 적용할 수 있음.
>>> 10 in (10,20,30,40)
True

>>> 3 in range(10)
True

>>> "P" in "Hello Python?"
True
```
2. 객체 연결하기(+)

    - 시퀸스 객체는 + 연산자를 이용해 두 개 이상을 연결할 수 있다.

```
>>> a = [1,2,3,4,5]
>>> b = [6,7,8,9]
>>> a + b
[1,2,3,4,5,6,7,8,9]

#단, 같은 타입인 경우에만 가능하며 range 는 지원하지 않음.

>>> range(1,5) + range(4,11) #error
```
![시퀸스 객체 연결하기](https://dojang.io/pluginfile.php/13491/mod_page/content/3/011004.png)


























3. 객체 반복하기 (*)

    - \* 연산자를 이용하여 시퀀스 객체를 반복할 수 있음.

```
>>> a = [1,2,3]
>>> a * 3
[1,2,3,1,2,3,1,2,3]

>>> b = "WoW"
>>> b * 3
WoWWoWWoW

# range는 안 됨.
```

4. 시퀸스 객체의 엘리먼트 개수 구하기

```
>>> a = [1,2,3,4]
>>> len(a)
4

>>> b = "HELLO KAKAO?"
>>> len(b) # ?
```

5. Index 사용하기.

    - 시퀀스 객체의 각 엘리먼트에 접근하는 방법으로 Index를 쓸 수 있음.

![인덱스의 개념](https://dojang.io/pluginfile.php/13494/mod_page/content/2/011010.png)
























```
>>> a = [10, 20, 30, 40, 50]
>>> a[0]    # 리스트의 첫 번째(인덱스 0) 요소 출력
10
>>> a[2]    # 리스트의 세 번째(인덱스 2) 요소 출력
30
>>> a[4]    # 리스트의 다섯 번째(인덱스 4) 요소 출력
50
>>> a[-1]
?

>>> b = (1,2,3,4)
>>> b[2]
3

>>> c = "Hello"
>>> c[3]
l

>>> r = range(1,10)
>>> r[5]
5
```

6. 엘리먼트 삭제 (del)
```
>>> a = [1,2,3,4,5]
>>> del a[0]
>>> a
[2,3,4,5]
```

7. Slice 사용하기

    - 시퀀스 객체의 일부를 잘라낼 때 사용

```
>>> a = [1,2,3,4,5,6,7,8,9,10]
>>> a[0:5]
[1,2,3,4]
```


> ## 딕셔너리 타입 변수(dictionary type)
- 연관된 값을 묶어서 저장할 필요가 있을 때.
    - 사람을 자료형으로 만들려면 어떻게 해야 할까?

```
name = "김사람"
age = 73
height = 192
weight = 33

# 그러면 사람이 두 명 이상이면?
```

```
person1 = {
    'name' : '김사람',
    'age' : 73,
    'height' : 192,
    'weight' : 33
}
```
```
# Dictionary 자료형의 기본 형태
dict = {'key' : 'value'}

```
- 키와 값(value)의 조건
  - 키 이름이 중복되면 나중에 정의된 값으로 덮어씀.
  - value 에는 어떤 값도 들어갈 수 있음.(숫자, 문자, 시퀀스 자료형..)
  - key에는 리스트, 딕셔너리 형태는 사용할 수 없음(그 외는 가능)

- 만드는 방법

```
>>> x = {}
>>> y = dict()
>>> x
{}
>>> y
{}

dict = dict(key1=value1, key2=value2 ...) # key는 따옴표로 묶이면 안 됨.
dict = dict(zip([key1,key2,key3, ...],[value1,value2,value3, ...]))
```

```
person = dict(name="김사람", age=73, height=192, weight=33)
person = dict(zip(["name","age","height","weight"], ["김사람",73,192,33]))
person = dict([("name","김사람"),("age",73),("height",192),("weight",73
)])
person = dict({'name' : '김사람', 'age' : 73, 'height' : 192, 'weight' : 33})
```