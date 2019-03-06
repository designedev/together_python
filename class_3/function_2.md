# 함수(function) - 2

- 함수의 결과를 반환하기.
```
def sum_num(a,b):
    sum = a + b
    print(sum)

sum_num(4,5) # 9를 출력.
# sum_num의 결과를 활용하고 싶다면?
```

- return 구문을 이용해, 결과를 반환할 수 있습니다.
```
def sum_num(a,b):
    sum = a + b
    return sum

sum_value = sum_num(3,5)
print(sum_value) # 8을 출력.    
```

- 코드가 수행되다가 return을 만나면 종료합니다.
```
def return_test():
    print("it will be shown")
    return
    print("can you see it?")
```

- 여러 개의 값을 한 번에 반환할 수도 있습니다.
```
def add_sub(a,b):
    sum = a + b
    sub = a - b
    return sum, sub

result = add_sub(3,4)
result # (7, -1)
```

- 몫과 나머지를 계산하는 함수를 만들어 봅시다.
```
a = 3
b = 10

def get_quotient_remainder:
    ..
    ..
    ..


quotient, remainder = get_quotient_remainder(a, b)
print("몫 : {0}, 나머지 : {1}".format(quotient, remainder))
```