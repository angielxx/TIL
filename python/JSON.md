# JSON 데이터 다루기

## loads()

: JSON 문자열을 Python 객체로 변환하는 함수

- 파일에 저장되어 있는 JSON 문자열을 읽거나, HTTP 요청의 전문(body)을 읽을 때 사용

### 예시

```python
import json

json_string = '''{
    "id": 1,
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874"
    },
    "admin": false,
    "hobbies": null
}'''

json_object = json.loads(json_string)

assert json_object['id'] == 1
assert json_object['email'] == 'Sincere@april.biz'
assert json_object['address']['zipcode'] == '92998-3874'
assert json_object['admin'] is False
assert json_object['hobbies'] is None
```



## load()

: JSON 파일을 Python 객체로 불러오기

### ### 예시

```python
# input.json

{
  "id": 1,
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874"
  },
  "admin": false,
  "hobbies": null
}
```

```python
import json

with open('input.json') as f:
    json_object = json.load(f)

assert json_object['id'] == 1
assert json_object['email'] == 'Sincere@april.biz'
assert json_object['address']['zipcode'] == '92998-3874'
assert json_object['admin'] is False
assert json_object['hobbies'] is None
```

