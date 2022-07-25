# 얕은 복사와 깊은 복사

### python에서 복사하는 방법

- 할당
- 얕은 복사
- 깊은 복사

## 할당

할당은 대입연산자 (`=`)를 이용하는 방법이다.

리스트를 대입연산자를 이용해 다른 변수에 할당하여 값을 확인해보자.

```python
original = [1, 2, 3]
copy = original
```

copy와 original은 값만 같은 다른 리스트일 것 같지만, 사실은

![image-20220725221056580](C:\Users\94app\AppData\Roaming\Typora\typora-user-images\image-20220725221056580.png)

대입연산자를 통한 복사는 해당 객체에 대한 '객체 참조'를 복사하기 때문에

```python
copy[0] = 'boo'
```

복사한 리스트의 값을 바꾸면 원본의 값까지 바뀌게 된다!

![image-20220725221228425](C:\Users\94app\AppData\Roaming\Typora\typora-user-images\image-20220725221228425.png)

## 얕은 복사

위에서 살펴 본 할당과 다르게 내용물을 다른 주소에 복사하여 원본 값에 영향을 주지 않는다.

### 슬라이싱을 이용하는 방법

```
original = [1,2,3]
copy = original[:]
```



![image-20220725222114602](C:\Users\94app\AppData\Roaming\Typora\typora-user-images\image-20220725222114602.png)

#### 2차원리스트 주의

2차원 리스트에서 리스트인 원소는 할당과 같이 객체 참조가 복사되어, 원본에 영향을 줄 수 있다.

```python
originl = [1,2,[3,4]]
copy = original[:]
```



![image-20220725222414081](C:\Users\94app\AppData\Roaming\Typora\typora-user-images\image-20220725222414081.png)

이럴 때는 깊은 복사를 사용해서 복사해야한다.!

## 깊은 복사

2차원의 리스트까지 다른 주소로 값을 복사하여 원본에 영향을 주지 않는다.

```python
import copy
original = [1,2,[3,4]]
copy = copy.deepcopy(original)
```

![image-20220725222807438](C:\Users\94app\AppData\Roaming\Typora\typora-user-images\image-20220725222807438.png)