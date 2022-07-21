# print() 함수의 옵션

```python
print(*objects, sep='', end='')
```



1. sep : print할 가변인자들 사이에 구분자(seperator)를 넣는 매개변수
2. end : 가변인자들을 모두 print하고 끝에 end에 넣은 문자열을 출력하는 매개변수



### sep

```python
print('S', 'E', 'P', sep='@')  # output : S@E@P
```



### end

end옵션의 특징은, end를 사용하면 그 다음 출력값은 줄바꿈을 하지 않고 출력된다는 것이다.

```python
print('I like', end=' ')
print('apple')

# output : I like apple
```

