# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨
# 파이썬에서 조건문 작성시 반드시 들여쓰기에 사용함을 명심

# 파이썬의 코드 블록
# 특정한 동작을 위해 관련된 코드를 한곳에 모아둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함!

# if 문
# if 조건식 :
#    조건이 참일 때 수행할 문장(들)

# 짝수 판별하기
num = int(input('숫자는? '))

if num % 2 == 0:
    print('짝수입니다')

if num % 2 == 0: print('짝수입니다') # 코드 간략화

# if ~ else
# if문은 조건이 참일 경우에만 지정한 코드를 실행하는데 비해
# if ~ else 문은 조건이 참일 때와 거짓일 때 각각 지정한 코드를
# 실행 한다는 것이 다름
# if 조건식 :
#    수행할 문장1
# else:
#    수행할 문장2

# 짝수 / 홀수 출력프로그램
num = int(input('숫자는? '))

if num % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')


# pass
# 조건문/반복문/함수/클래스나 다른 문등에서
# 실행문이 정해지지 않은 경우 임시로 작성하는 명령문

if num % 2 == 0:
    pass
else:
    pass


# 마일리지 사용하기
mileage = 1200

# if mileage > 1000:
#    print('마일리지 사용 가능!')
#else:
#    print('마일리지 사용 불가!')

# result = ''
# if mileage >= 1000:
#     result = '마일리지 사용 가능!'
# else:
#     result = '마일리지 사용 불가!'

# print(result)

result = '마일리지 사용 불가!'
if mileage >= 1000:
    result = '마일리지 사용 가능!'

print(result)

# 중첩 if 문
# if문 속에 또 다른 문을 포함시켜 작성하는 조건문
# 조건문을 중첩할 때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을 때 사용 - 복잡함

# 평균 점수에 따라 ABCDF 학점을 처리하는 조건문 작성
avg = 73.5

grade = 'F'
if avg >= 90:
    grade = 'A'
else:
    if avg >= 80:
        grade = 'B'
    else:
        if avg >= 70:
            grade = 'C'
        else:
            if avg >= 60:
                grade = 'D'

print(grade)


# 다중 if문
# 주첩 if문을 작성하는 경우, 조건이 많으면 다소 복잡함
# 이러한 중첩 if문을 단순하게 작성할 수 있는 조건문
# if 조건1 :
#      실행할 코드1
# elif 조건2:
#      실행할 코드2
# elif 조건3:
#      실행할 코드3
# elif 조건4:
#      실행할 코드4

avg = 85.5

grade = 'F'
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'

print(grade)

# if 조건문 대체 1 - switch 모방
# 조건이 많아 지는 경우, 다중 조건문 역시 복잡해 짐
# 이럴 경우, dict 자료구조를 이용하면 간단하게 작성 가능

# if 조건문 대체 2
# py 3.10부터 switch와 비슷한 match ~ case 문 도입
# match 값:
#   case 값 범위1: 실행문1
#   case 값 범위2: 실행문2
#   default: 실행문2

# 주민번호 성별 코드에 따른 성별 출력
# 1: 남자 (2000년 이전 출생)
# 2: 여자 (2000년 이전 출생)
# 3: 남자 (2000년 이후 출생)
# 4: 여자 (2000년 이후 출생)

code = int(input('성별코드는? '))

result = ''
match code:
    case 1: result = '남자 (2000년 이전 출생)'
    case 2: result = '여자 (2000년 이전 출생)'
    case 3: result = '남자 (2000년 이후 출생)'
    case 4: result = '여자 (2000년 이후 출생)'
    case _: result = '외국인이군요!'

print(result)


# 다중 if 문으로 작성한 학점계산 코드를
# match case로 바꿔 작성해보세요

grade = int(input('학점을 입력하세요.'))

result = 'F'
avg = 85.5

match int(avg/10):
    case 10 | 9: grade = 'A'
    case 8: grade = 'B'
    case 7: grade = 'C'
    case 6: grade = 'D'
    case _: grade = 'F'

print(grade)


# 속도 위반 경고
speed = int(input('자동차의 현재 속도는 : '))

weban = ''
if speed >= 50:
    weban = '속도 위반!!'

print(weban)


# 자동 온도 조절 장치
ondo = int(input('기계 온도를 입력하세요 : '))

fen = ''
if ondo >= 40:
    fen = '가동'
else:
    if ondo <= 40:
        fen = '중지'

print(f'팬(Fan){fen} ')


# 자동 주문 시스템
auto = int(input('Good morning.\n Nice meet you.\n Where are you from?\n Plese select a number\n 1.대한민국 2.USA 3. 中國 '))

lag = ''
if auto == 1:
    leg = '주문하시겠어요?'
elif auto == 2:
    leg = 'Would you like to order?'
elif auto == 3:
    leg = '您要点菜吗？'
else:
    leg = ('SORRY, I m not applying'
           'Please choose between 12 and 3.')

print(leg)


# 국가 재난지원금 수령액 조회
family = int(input('인원수를 입력하세요.'))

result = '1,000,000원 지원'
if family == 1:
    result = '400,000원 지원'
if family == 2:
    result = '600,000원 지원'
if family == 3:
    result = '800,000원 지원'

print(result)

# 개선된 BMI 지수 출력
bmi = float(input('BMI 지수를 입력하세요 : '))

result = '저체중'
if bmi <= 140:
    result = '고도비만'
elif bmi > 120:
    result = '비만'
elif bmi > 110:
    result = '과체중'
elif bmi > 90:
    result = '정상체중'

print(f'BMI 지수 : {bmi}, 진단 결과 : {result} 입니다.')


# 버스 전용차로 단속
msg1 = '''1. 월~금, 2. 토요일, 3. 공휴일
요일을 선택하세요.'''
msg2 = '''버스 전용차로 단속 중 입니다.
1.버스, 2.승용차'''
msg3 ='버스 전용차로 위반!'
msg4 ='버스 입니다.'
msg5 ='토요일 및 공휴일은 단속하지 않습니다.'

dayweek = int(input(msg1))

result = ''
if dayweek == 1: # 평일 여부 확인
    carType = int(input(msg2))
    if carType != 1:           # 차량 종류 확인
        result = msg3
    else:
        result = msg4
else:
    result = msg5

print(result)


# 마스크 구매 가능 요일 출력
endBirthYear = int(input('출생연도 끝자리 입력 : '))
age = int(input('만 나이 입력 : '))
result = ''
if age < 65:
    # if endBirthYear == 1 or endBirthYear == 6:
    #    result = '월요일 구매 가능합니다'
    # elif endBirthYear == 2 or endBirthYear == 7:
    #  result = '화요일 구매 가능합니다'
    # elif endBirthYear == 3 or endBirthYear == 8:
    #     result = '수요일 구매 가능합니다'
    # elif endBirthYear == 4 or endBirthYear == 9:
    #     result = '목요일 구매 가능합니다'
    # elif endBirthYear == 5 or endBirthYear == 0:
    #     result = '금요일 구매 가능합니다'
    match endBirthYear:
        case 1 | 6:
            result = '월요일 구매 가능합니다'
        case 2 | 7:
            result = '화요일 구매 가능합니다.'
        case 3 | 8:
            result = '수요일 구매 가능합니다.'
        case 4 | 9:
            result = '목요일 구매 가능합니다.'
        case 5 | 0:
            result = '금요일 구매 가능합니다.'


print(result)


# 차량 2부제
from _datetime import datetime
# day = int(input('오늘은 몇일? '))
day = datetime.today().day
carNum = int(input('차량 번호 4자리는? '))

msg1 = '오늘 입차 : 번호가 홀수인 차량'
msg2 = '귀하의 차량은 입차 불가능합니다.'
if day % 2 == 0:
    msg1 = '오늘 입차 : 번호가 짝수인 차량'

if day % 2 == carNum % 2:
    msg2 = '귀하의 차량은 입차 가능합니다.'

print(f'''오늘 날짜 : {day} 일')
{msg1}
{msg2}''')



# 생존율 출력
msg = '최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요.'
time = int(input(msg))

result = '25% 미만'
if time <= 60: result = '85%'
elif time <= 120: result = '76%'
elif time <= 180: result = '66%'
elif time <= 240: result = '57%'
elif time <= 300: result = '47%'
elif time <= 360: result = '35%'

print(result)


# 전기 요금 계산기
basePrice = 0   # 기본 요금
unitPrice = 0   # 단가
PowerPrice = 0  # 전기 요금

powerAmount = int(input('전기 사용량은?'))

if powerAmount > 400:
    basePrice = 7300
    unitPrice = 280.6
elif powerAmount > 200:
    basePrice = 1600
    unitPrice = 187.9

PowerPrice = basePrice + (unitPrice * powerAmount)

print(f'''
사용량 : {powerAmount} kwh
기본요금 : {basePrice} 원
단가 : {unitPrice} 원
★전기 요금★ : {PowerPrice}''')
