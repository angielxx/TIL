# PEP8 : Code Style Guide

- [PEP8](https://peps.python.org/pep-0008/) : 공식적으로 파이썬에서 제안하는 스타일 가이드이다.

## 1. 들여쓰기

들여쓰기 : 4개의 스페이스 (= 탭 한번)

- 첫번째 줄에 인자가 있으면 수직정렬하여 읽기 좋게 만듭니다.
- 첫번째 줄에 인자가 없다면, 추가로 들여쓰기를 하여 다음행과 구별이 되도록 해야 합니다.

## 2. 주석

- 코드에 대한 설명으로, 개발자를 위한 것
- 초기부터 주석을 다는 습관을 들여야한다!

#### 주석 문법

한줄 주석 : `# Text`

여러줄 주석 : `""" Text """` (단축키 : `ctrl` + `/`)

#### 주석 작성하는 규칙

- 첫 글자는 대문자 (소문자로 시작하는 변수일 경우, 소문자로 시작)
- Inline comment는 짧게

## 3. Naming Convention

leading underscores(앞에 있는 _)와 trailing underscores(뒤에 있는 _)를 파이썬에서 사용할 때 다음과 같이 사용할 수 있습니다.

- _single_leading_underscore : 내부적으로 사용하는 변수를 의미할 때 앞에 언더스코어(_)를 넣습니다
- single_trailing_underscore_ : 파이썬에서 기본 키워드와 겹치는 것을 피하려면 마지막에 언더스코어를 넣습니다.
- __double_leading_underscore : 더블 언더스코어(__)는 name mangling과 관련된 것입니다.