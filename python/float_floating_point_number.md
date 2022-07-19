# Float (floating point number)

`float`은 실수다.

## 실수 연산시 주의할 점!!

### Floating Point Number

: 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하기 때문에, 어떠한 값이 항상 같은 값으로 일치되지 않는다. 

```python
print(3.5 - 3.12 == 0.38) #False
```

위 코드의 출력값은 `False`이다.



### 해결책

#### 1. 임의의 작은 수를 사용

```python
a = 3.5 - 3.12
b = 0.38

print(abs(a - b) <= 1e-10) #True
```

* `abs()` : 절대값을 구하는 함수
* `1e-10` : 컴퓨터식 지수 표현 방식! (e =10)



#### 2. sys 모듈 사용

- sys : 
- `sys.float_info.epsilon` : 이 곳에 저장된 값은 '머신 엡실론(machine epsilon)'이다. 머신 엡실론은 반올림 오차의 상한값이며 연산한 값과 비교할 값의 차이가 머신 엡실론보다 작거나 같다면 두 실수는 같은 값이라 할 수 있다.

```python
import sys
print(abs(a - b) <= sys.float_info.epsilon) #True
```



#### 3. math모듈을 사용 (python 3.5+)

```python
import math
print(math.isclose(a, b)) # True
```

