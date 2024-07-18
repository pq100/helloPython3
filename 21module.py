# 모듈
# 매우 복잡하고 긴 파일을 하나의 파일에
# 모두 작성하는 것은 비효율적일 수 있음 - 유지보수 힘듦
# 또한, 여러 사람들과 함께 개발하는 경우
# 작업분담, 작업결과물 통합 역시 어려움

# 모듈 방식의 개발을 이용하면
# 사용 용도에 따라 파일별로 나눠 작성 가능
# 타인이 만들어 둔 코드를 자신의 프로그램에서 활용 가능
# 따라서, 모듈은 변수/함수/클래스들을 모아둔 파일

# 모듈은 현재 디렉토리에 있는 파일이나
# 파이썬 라이브러리 디렉토리에 있는 파일을 불러올 수 있음
# 사용자/venv/py310/Lib/site-package
# 모듈명.함수명,모듈명.클래스 형식으로 코드 작성

import snicuz.hello

snicuz.hello.sayHello()

# ---

from snicuz import hello

hello.sayHello()

# --
from snicuz2 import hello2

hello2.sayHello2()


# 모듈 사용하기 1 - 모듈명.함수명
import snicuz

val = snicuz.calc.add(10, 5)
print(val)

# 모듈사용하기 2 - 함수명
from snicuz.calc import add
from snicuz.calc import div

val = add(10, 5)
print(val)
val = div(10, 5)
print(val)

# 모듈사용하기 3 - 함수명
from snicuz.calc import  *

val = mul(10,5)
print(val)
val = minus(10,5)
print(val)

# 모듈사용하기 4 - 함수명
import snicuz.calc as zc

val = zc.add(10, 20)
print(val)

# 외부 모듈 사용하기
# 내장 모듈이나 사용자 정의 모듈 이외에
# 다른 조직 / 기관이나 개인이 만든 모듈을 사용하려면
# 'pip install 모듈명'으로 설치하면 됨
# pip install scikit-learn
# pip install pymysql
# pip install fastapi

# snicuz.example에 각 문제에 대한 모듈 작성
# 단위 환산 (convertUnit/readUnit/printUnits)
import snicuz.example as zex

import snicuz.example as zex

mm = zex.readUnit()
units = zex.converUnit(mm)
zex.printUnits(units)

# 할인된 상품 가격표 출력 (discountPrice/readDiscount/printPrices)
products = {'쌀':9900, '상추':1900, '고추':2900, '마늘':8900, '통닭':5600, '햄':6900, '치즈':3900}
def readDiscount():
    print('''
    ----------------------------------
    -- 한빛 마트 오늘의 할인 가격표 출력 --
    ----------------------------------
    ''', end='')
    rate = float(input('오늘의 할인율은? '))
    return rate

def printPrice(dcprice, rate):
    result = ''
    for idx, k in enumerate(products):
        result += f'{k:4s} : {products[k]:,d} 원 {rate} % DC -> {dcprice[idx]:,.0f} 원\n'
        print(result)

def discountPrice(rate):
    dcprice = []
    dc = (1 - (rate / 100))
    for v in products.values():
        dcprice.append( v * dc )
    return dcprice

rate = readDiscount()
dcprice = discountPrice(rate)
printPrice(dcprice, rate)


# 주민번호 유효성 체크
# 주민등록번호는 13자리로 이루어져 있으며, 앞 6자리는 생년월일, 뒤 7자리 중 첫 번째 숫자는 성별 코드, 나머지 6자리는 지역 및 순서 코드를 의미합니다.
# 유효한 주민등록번호인지 확인하기 위해서는 다음과 같은 규칙을 따릅니다.
# 주민등록번호 길이가 13자리인지 확인합니다.
# 뒤 7자리 중 첫 번째 숫자가 1, 2, 3, 4 중 하나인지 확인합니다. (1, 3은 남자, 2, 4는 여자를 의미)
# 뒤 7자리 중 첫 번째 숫자를 제외한 나머지 6자리가 유효한 값인지 확인합니다. (000001 ~ 899999 사이의 값)
# 주민등록번호 유효성 검사 공식에 따라 계산한 결과가 맞는지 확인합니다.
# 이 때 주민등록번호 유효성 검사 공식은 다음과 같습니다.

# 주민등록번호 앞 12자리에 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 곱한 값을 모두 더하고
# 그 결과값을 11로 나눈 나머지를 11에서 뺍니다.
# 계산 결과값이 주민등록번호 마지막 자리 숫자와 일치하면 유효!
# 1 2 3 4 5 6 - 1 2 3 4 5 6 7
# * * * * * *   * * * * * * *
# 2 3 4 5 6 7   8 9 2 3 4 5
# 2+6+12+20+30+42+8+18+6+12+20+30
# 11 - (206 % 11) = 3 ? 7
# (checkJumin/readJumin/printJumin)

sum = 0
result = '주민번호 불일치!'

jumin = input('주민번호는? (xxxxxxyyyyyyy)')
sum += int(jumin[0]) * 2
sum += int(jumin[1]) * 3
sum += int(jumin[2]) * 4
sum += int(jumin[3]) * 5
sum += int(jumin[4]) * 6
sum += int(jumin[5]) * 7
sum += int(jumin[6]) * 8
sum += int(jumin[7]) * 9
sum += int(jumin[8]) * 2
sum += int(jumin[9]) * 3
sum += int(jumin[10]) * 4
sum += int(jumin[11]) * 5

checker = (11 - (sum % 11)) % 10
if checker == int(jumin[12]): result = '주민번호 유효!'
print(result)

def checkJumin(Jumin):
    result = '주민번호 불일치!'
    sum = 0

    weight = [2,3,4,5,6,7,8,9, 2,3,4,5]

    for i in range(13):
        sum += int(jumin[i]) * weight[i]

    checker = (11 - (sum % 11)) % 10
    if checker == int(jumin[12]): result = '주민번호 유효!'

    return result

import snicuz.example as zex

zex.checkJumin('1234561234567')

# zex.checkJumin2('123456-1234567')