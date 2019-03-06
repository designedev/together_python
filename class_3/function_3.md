# 함수(function) - 3

- 위치 인수와 키워드 인수의 이해
```
print(10,20,30) # 매개변수를 순서대로 넣는 방식을 위치 인수라고 합니다.
# 10 20 30




def print_info(name, age, address):
    print("이름 : {0}".format(name))
    print("나이 : {0}".format(age))
    print("주소 : {0}".format(address))


print_info(name="김퍼스널", age=7, address="남산타워 3층") # 인수의 이름을 직접 지정해 주는 방식을 키워드 인수라고 합니다.

# 이름 : 김퍼스널
# 나이 : 7
# 주소 : 남산타워 3층

sum_num(4,5) # 9를 출력.
# sum_num의 결과를 활용하고 싶다면?
```

- 위치 인수와 리스트 언패킹
```
def sum_num(a, b, c):
    sum = a + b + c
    return sum

x = [10,20,30]

#sum_num의 매개변수로 x를 사용하고 싶다면?
```

- 가변 인수 함수 만들기 (인자가 정해져 있지 않다면?)
```
def print_numbers(*args): #위의 리스트 언패킹을 응용
    for arg in args:
        print(arg)
```
