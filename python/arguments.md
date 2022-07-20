# 정해지지 않은 여러개의 Arguments를 처리하는 방법

## 가변인자 (*args)

- 여러개의 positional argument를 하나의 필수 parameter로 받아서 사용
- 몇 개의 positional argument를 받을지 모르는 함수를 정의할 때



### 패킹/언패킹

#### 패킹

- 여러개의 데이터를 묶어서 변수에 할당

```python
numbers = (1, 2, 3, 4, 5) # 패킹
print(numbers) # (1, 2, 3, 4, 5)
```

#### 언패킹

- 시퀀스 속 요소들을 여러개의 변수에 나누어 할당하는 것

##### 주의할 점

1. 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함

```python
numbers = (1, 2, 3, 4, 5)
a, b, c, d, e = numbers # 언패킹
print(a, b, c, d, e) # 1 2 3 4 5
```

2. 언패킹시 변수의 왼쪽에 asterisk( `*` )를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음

```python
numbers = (1, 2, 3, 4, 5)

a, b, *rest = numbers
print(a, b, rest) # 1 2 [3, 4, 5]

a, *rest, e = numbers
print(a, rest, e) # 1 [2, 3, 4] 5
```

### Asterisk와 가변인자

- `*` 는 시퀀스 언패킹 연산자 (시퀀스를 풀어 헤치는 연산자)
  - 주로 튜플이나 리스트를 언패킹하는데 사용한다.

```python
def func(*args):
    print(args)
    print(type(args))
    
func(1, 2, 3, 'a', 'b')
'''
(1, 2, 3, 'a', 'b')
<class 'tuple'>
'''
```

#### 가변인자 활용

: 반드시 받아야하는 인자와, 추가적인 인자를 구분해서 사용할 수 있다.

```python
def print_family_name(father, mother, *pets):
	print(father)
	print(mother)
	print(pets)
	...
	
print_family_name('아부지', '어머니', '멍멍이', '야옹이')
```



## 가변 키워드 인자 (**kwargs)

- 몇 개의 키워드 인자를 받을 지 모르는 함수를 정의할 때 유용
- `**kwargs`는 딕셔너리로 묶어 처리

```python
def family(**kwargs):
	for key, value in kwargs.items():
		print(key, ":", value)
		
print(father='아빠', mother='엄마', baby='아가')
'''
father : 아빠
mother : 엄마
baby : 아가
'''
```

### 주의할 점

- key는 'father'이 아니라 father (문자열로 쓰지 말 것)



## 가변 인자와 가변 키워드 인자의 동시 사용

```python
def print_family_name(*parents, **pets):
	print('아버지 :', parents[0])
	print('어머니 :', parents[1])
	if pets:
		print('반려동물들..')
		for title, name in pets.items():
			print('{} : {}'.format(title, name))
```

