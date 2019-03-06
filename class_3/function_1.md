# 함수(function) - 1

> ## 특정 용도를위한 코드를 한 곳에 모아둔 것
- 몇 줄의 문장을 출력할 일이 있을 떄

```
print("Lorem ipsum dolor sit amet, consectetur adipisicing elit,")
print("sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
print("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris")
print("nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in")
print("reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla")
print("pariatur. Excepteur sint occaecat cupidatat non proident,")
print("sunt in culpa qui officia deserunt mollit anim id est laborum.")
```

- 이런 문장을 여러 번 출력해야 한다면?
```
1. print 문을 횟수만큼 반복한다.
2. for 문을 이용해 원하는 횟수만큼 반복한다.
3. "함수" 를 이용한다.
```

- 이럴 때 함수를 사용합니다.
```
def 함수이름():
    수행할 코드



def print_lorem():
    print("Lorem ipsum dolor sit amet, consectetur adipisicing elit,")
    print("sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    print("Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris")
    print("nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in")
    print("reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla")
    print("pariatur. Excepteur sint occaecat cupidatat non proident,")
    print("sunt in culpa qui officia deserunt mollit anim id est laborum.")


print_lorem() # def 뒤에 정의한 이름으로 실행할 수 있습니다.
```


- 함수는 자유롭게 사용할 수 있지만, 실행 순서가 있습니다.
```
- 함수 선언이 되었다고 해서 바로 실행되지는 않음.
- 함수를 실행하는 명령문에 의해 수행됨.
- 선언이 되지 않은 함수를 실행할 수 없음.
```

- 함수는 아래와 같은 순서로 수행됩니다.
![함수의 실행구조](https://dojang.io/pluginfile.php/13778/mod_page/content/3/029001.png)




















- 아래와 같이, 함수를 정의하기 전에 실행하면 오류가 발생합니다.
```
hello() # Error!

def hello():
    print("Hello World?")

hello() # Hello World? 가 출력됨.
```

- 함수의 파라미터(매개변수) 정의하고 사용하기

세 개의 수를 더한 결과를 출력하고 싶다면?
```
a = 10
b = 5
c = 8
sum = a+b+c
print(sum)
```
이런 출력을 여러 개의 경우에 대해 매번 수행해야 한다면?
```
a = 1
b = 2
c = 5
d = 39
e = 21
f = 48
g = 31
# a + b + c 를 출력
# b + e + f 를 출력
# e + e + e 를 출력
..
..
..
```
정의된 매개변수를 입력받아 동작을 수행하는 함수를 만들어서 해결할 수 있습니다.
```
def 함수이름(매개변수1, 매개변수2...):
    코드

def sum_three_numbers(a,b,c):
    sum = a + b + c
    print(sum)


sum_three_numbers(a,b,c)
sum_three_numbers(b,e,f)
sum_three_numbers(e,e,e)
..
..
```

- 함수를 사용해 반복되는 작업을 간편히 해결할 수 있는 예를 생각해 봅시다.
