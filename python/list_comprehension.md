# List comprehension

: 리스트 표현식

- 파이썬의 리스트의 특징 : 리스트 안에 for문과 if문을 사용할 수 있다는 것
- 리스트 표현식으로 리스트를 간편하게 생성할 수 있다.

### 기본 문법

```python
[ 식 for 변수 in iterable ]
list( 식 for 변수 in iterable )
```

** iterable : 순회할 수 있는 값



#### 예시

```python
# 1부터 10까지의 값의 제곱수를 값으로 가지는 리스트
# [ 1, 4, 9, 16, 25, 36, 49, 64, 81]

list1 = [ n ** 2 for n in range(1, 11) ]
list2 = list( n ** 2 for n in range(1. 11))
```



## 리스트 표현식에 조건문 활용하기

리스트 표현식에 if 조건문을 넣어, 조건에 부합하는 값만 리스트에 넣음으로써 filter 함수와 같은 기능을 할 수 있다.



### 문법

```python
[ 식 for 변수 in iterable if 조건식]
list( 식 for 변수 in iterable if 조건식 )
```

![img](https://dojang.io/pluginfile.php/13698/mod_page/content/2/022017.png)

## for문과 if문을 여러 번 사용하기

### 문법

```python
[식 for 변수1 in 리스트1 if 조건식1     for 변수2 in 리스트2 if 조건식2     ...     for 변수n in 리스트n if 조건식n]
 
list(식 for 변수1 in 리스트1 if 조건식1         for 변수2 in 리스트2 if 조건식2         ...         for 변수n in 리스트n if 조건식n)
```



### 예시

```python
a = [i * j for j in range(2, 10) for i in range(1, 10)]
a = [i * j for j in range(2, 10)
           for i in range(1, 10)]
# a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
```

- 위 코드는 [ 구구다 2단 + 3단 + ... + 8단 + 9단 ]의 리스트를 생성하는 방법이다.

- 여러 줄로 작성하면 가독성이 좋아진다. 들여쓰기는 필수는 아니다.![img](https://dojang.io/pluginfile.php/13698/mod_page/content/2/022018.png)