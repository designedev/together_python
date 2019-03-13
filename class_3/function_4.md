# 함수(function) - 4

- 함수의 재귀호출(Recursive call)
함수가 자기 자신을 호출하는 형태입니다.
일반적으로 자주 쓰지 않지만, 유용하게 사용할 수 있는 상황이 있습니다.
(계승(factorial), 피보나치 수열 등..)
```
def recursive_test():
        print("hello")
        recursive_test()


recursive_test()
```
![재귀함수 호출구조](https://dojang.io/pluginfile.php/13846/mod_page/content/2/031001.png)

- 재귀 호출의 종료 조건 만들기
```
def recursive_test(count):
        if(count == 0):
                return
        else:
                print("hello")
                recursive_test(count-1)
```

- 재귀 호출로 팩토리얼 계산하기
계승은 [이것](https://ko.wikipedia.org/wiki/%EA%B3%84%EC%8A%B9)입니다..
```
def factorial(num):
...
...
...
...
```

- 팩토리얼 계산이 완벽하게 이해가 되셨다면, [피보나치 수열](https://ko.wikipedia.org/wiki/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98_%EC%88%98)을 계산해 봅시다.
```
def fibonacci(index, first, second):
...
...
...
```