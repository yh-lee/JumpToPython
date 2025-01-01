# "Life is too short, You need Python"
# "a"
# "123"

## 큰따옴표로 양쪽 둘러싸기
# "Hello World"

## 작은따옴표로 양쪽 둘러싸기
# 'Python is fun'

## 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
# """Life is too short, You need python"""

## 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
# '''Life is too short, You need python'''

## 문자열에 작은따옴표 포함하기
# Python's favorite food is perl
# food = "Python's favorite food is perl"
# print(food)

## 문자열에 큰따옴표 포함하기
# say = '"Python is very easy." he says.'
# print(say)

## 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기
# food = 'Python\'s favorite food is perl'
# say = "\"Python is very easy.\" he says."
# print(food)
# print(say)

## 여러 줄인 문자열을 변수에 대입하고 싶을 때
# multiline = "Life is too short\nYou need python"
# print(multiline)

##  연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
# multiline='''
# Life is too short
# You need python
# '''
# multiline="""
# Life is too short
# You need python
# """
# print(multiline)

## 문자열 더해서 연결하기
# head = "Python"
# tail = " is fun!"
# print(head + tail)

## 문자열 곱하기 응용
# print("=" * 50)
# print("My Program")
# print("=" * 50)

## 문자열 길이 구하기
# a = "Life is too short"
# print(len(a))

## 문자열 인덱싱
# a = "Life is too short, You need Python"
# print(a[0])
# print(a[3])
# print(a[-1])
# print(a[-0])
# a = "Life is too short, You need Python"
# b = a[0] + a[1] + a[2] + a[3]
# print(b)
# a = "Life is too short, You need Python"
# print(a[0:4])

## 문자열을 슬라이싱하는 방법
# a = "Life is too short, You need Python"
# print(a[0:5])
# print(a[0:2])
# print(a[5:7])
# print(a[12:17])
# print(a[19:])
# print(a[:17])
# print(a[:])
# print(a[19:-7])

## 슬라이싱으로 문자열 나누기
# a = "20230331Rainy"
# date = a[:8]
# weather = a[8:]
# print(date)
# print(weather)
# year = a[:4]
# day = a[4:8]
# weather = a[8:]
# print(year)
# print(day)
# print(weather)

### 문자열 포매팅

## 숫자 바로 대입
# print("I eat %d apples." % 3)

## 문자열 바로 대입
# print("I eat %s apples." % "five")

## 숫자 값을 나타내는 변수로 대입
# number = 3
# print("I eat %d apples." % number)

## 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate %d apples. so I was sick for %s days." % (number, day))

## 문자열 포맷 코드
# "I have %s apples" % 3
# "rate is %s" % 3.234

### 포맷 코드와 숫자 함께 사용하기
## 정렬과 공백
# print("%10s" % "hi")
# print("%-10sjane." % 'hi')

## 소수점 표현하기
# print("%0.4f" % 3.42134234)
# print("%10.4f" % 3.42134234)

## format 함수를 사용한 포매팅
# print("I eat {0} apples".format("five"))

## 숫자 값을 가진 변수로 대입하기
# number = 3
# print("I eat {0} apples".format(number))

##
# 2개 이상의 값 넣기
# number = 10
# day = "three"
# print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

## 이름으로 넣기
# print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

## 인덱스와 이름을 혼용해서 넣기
# print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))

## 왼쪽 정렬
# print("{0:<10}".format("hi"))

## 오른쪽 정렬
# print("{0:>10}".format("hi"))

## 가운데 정렬
# print("{0:^10}".format("hi"))

## 공백 채우기
# "{0:=^10}".format("hi")
# "{0:!<10}".format("hi")

## 소수점 표현하기
# y = 3.42134234
# print("{0:0.4f}".format(y))
# print("{0:10.4f}".format(y))

## { 또는 } 문자 표현하기
# print("{{ and }}".format())

## f 문자열 포매팅
# name = '홍길동'
# age = 30
# print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
# print(f'나는 내년이면 {age + 1}살이 된다.)
# d = {'name':'홍길동', 'age':30}
# print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
# print(f'{"hi":<10}')
# print(f'{"hi":>10}')
# print(f'{"hi":^10}')
# print(f'{"hi":=^10}')
# print(f'{"hi":!<10}')
# y = 3.42134234
# print(f'{y:0.4f}')
# print(f'{y:10.4f}')

### 문자열 관련 함수들
## 문자 개수 세기 - count
# a = "hobby"
# print(a.count('b'))

## 위치 알려 주기 1 - find
# a = "Python is the best choice"
# print(a.find('b'))
# print(a.find('k'))

## 문자열 삽입 - join
# print(",".join('abcd'))
# print(",".join(['a', 'b', 'c', 'd']))

## 소문자를 대문자로 바꾸기 - upper
# a = "hi"
# print(a.upper())

## 대문자를 소문자로 바꾸기 - lower
# a = "HI"
# print(a.lower())

## 왼쪽 공백 지우기 - lstrip
# a = " hi "
# print(a.lstrip())

## 오른쪽 공백 지우기 - rstrip
# a= " hi "
# print(a.rstrip())

## 양쪽 공백 지우기 - strip
#  a = " hi "
# print(a.strip())

## 문자열 바꾸기 - replace
# a = "Life is too short"
# print(a.replace("Life", "Your leg"))

## 문자열 나누기 - split
# a = "Life is too short"
# print(a.split())
# b = "a:b:c:d"
# print(b.split(':'))

