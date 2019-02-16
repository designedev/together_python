# 반복문(for, while) 사용하기.

> ## 조건을 만족할 때까지 코드를 반복 실행합니다.

- "Go Home!" 을 100번 출력하는 방법(1)

```
print("Go Home!")
print("Go Home!")
print("Go Home!")
print("Go Home!")
print("Go Home!")
# ... 100번 반복 ...
# 이건 아니다...
```

- 이럴 때 for 문을 사용해서 간단하게 처리할 수 있습니다.
```
# range 를 사용.
for value in range(100):
    print("Go Home!")    

# 리스트 사용.
var_list = [10,20,30,40]
for value in var_list:
    print("Go Home!")

# 튜플 사용.
var_tuple = ("apple", "orange", "grape")
for fruit in var_tuple:
    print(fruit)

# 문자열 사용.
var_string = "STUDENTS"
for letter in var_string:
    print(letter, end = ' ')
```

![for 문의 동작구조](https://dojang.io/pluginfile.php/13592/mod_page/content/4/016002.png)























- "Go Home!" 을 100번 출력하는 방법(2)
```
#while 을 사용.
counter = 0
while counter < 100:
    print("Go Home!")
    counter = counter + 1 # 반복되는 코드 안에 조건을 변화시키는 코드가 꼭 있어야 함.
    # 없으면 어떻게 될까요?
```

![while 문의 동작구조](https://dojang.io/pluginfile.php/13600/mod_page/content/3/017001.png)




















> ## 반복문을 사용한 예
```
range_val = range(1,10)
factor_val = 2
for i in range_val:
    print(str(factor_val) + " X " + str(i) + " = " + str(i * factor_val))
```