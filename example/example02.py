# 할당 연산자

# 논리 연산자
# 논리 AND (&&): 모든 조건이 true일 때만 전체 조건이 true가 되는 연산자입니다.
# 예를 들어, A && B는 A와 B가 모두 true일 때 true가 됩니다.
# 논리 OR (||): 하나 이상의 조건이 true이면 전체 조건이 true가 되는 연산자입니다.
# 예를 들어, A || B는 A 또는 B 중 하나라도 true면 true가 됩니다.
# 논리 NOT (!): 주어진 조건의 반대 값을 반환하는 연산자입니다.
# 예를 들어, !A는 A가 true이면 false를 반환하고, A가 false이면 true를 반환합니다.

# 논리 연산자 단축식 평가

# 삼항 연산자
# 조건문을 한 줄로 표현할 수 있는 연산자
# 참일때 값 if 조건식 else 거짓일때 값



# 4
x = 1; y = 2; z = 3
s0 = 1; v0 = 2; t = 3; g = 9.8

a = 3 * x
b = 3 * x + y
c = (x + y) / 7
d = (3 * x + y) / (z + 2)
e = s0 + v0 * t + 1/2 * g * t ** 2



# 5 ~ 10


# 12

currentYear = int(input('현재년도는? '))
birthYear = int(input('생일의 년도는? '))
isPass = bool(input('생일의 지남 여부는? (True/False) '))

myAge = currentYear - birthYear
# myAge = myAge if (isPass == True) else (myAge - 1)
myAge = myAge if isPass else (myAge - 1)

print(f'''현재년도가 {currentYear}이고,
생일의 년도가 {birthYear}일 때,
나이는 {myAge} 세 입니다.''')


# 14
day = 86400    # 하루 - 초
hour = 3600    # 시간 - 초
minute = 60    # 분 - 초

days = 1234567890 / day
hour = 98765 / hour
minute = 12345 / minute

print(f'''
{int(days):,}일
{int(hour):,}시
{int(minute):,}분
''')

# 16 (!!)

price = 3_4650
paid = 50_000
charge = paid - price


# w50000 = charge / 50000         # 결과는 float
# w50000 = int(charge / 50000)    # 결과를 정수형으로 변환
w50000 = charge // 50000          # 파이썬의 몫 연산자
# charge = charge - (50000 * w50000)
charge %= 50000

w10000 = charge // 10000
# charge = charge - (10000 * w10000)
charge %= 10000

w5000 = charge // 5000
# charge = charge - (5000 * w5000)
charge %= 5000

w1000 = charge // 1000
# charge = charge - (1000 * w1000)
charge %= 1000

w500 = charge // 500
# charge = charge - (500 * w500)
charge %= 500

w100 = charge // 100
# charge = charge - (100 * w100)
charge %= 100

w50 = charge // 50
# charge = charge - (50 * w50)
charge %= 50

w10 = charge // 10
# charge = charge - (10 * w10)
charge %= 10

print(f'''
금액 : {price:,} 원
지불 금액 : {paid:,} 원
잔돈 : {paid - price:,} 원
---------------------------
50000원 : {w50000} 장
10000원 : {w10000} 장
5000원 : {w5000} 장
1000원 : {w1000} 장
500원 : {w500} 원
100원 : {w100} 원
50원 : {w50} 원
10원 : {w10} 원
''')