# 수식/표현식 expression
# 숫자, 변수, 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 산술연산자
# 자료형 승격promotion

# 매출액 입력시 총합을 출력

# 문제 해결 5-2 1분기 수익 계산하기
bungi1 = int(input('1월 매출 : '))
bungi2 = int(input('2월 매출 : '))
bungi3 = int(input('3월 매출 : '))

malip = int(input('1분기 매입 : '))

sulik = bungi1 + bungi2 + bungi1 - malip

print(f'수익 : {sulik} 원')


# 문제 해결 5-3 방의 넓이 구하기

galo = int(input('가로 길이: '))
selo = int(input('세로 길이: '))

nubi = galo * selo

print(f'넓이 : {nubi} cm제곱')


# 문제 해결 5-4 신체질량지수(BMI) 구하기

weight = int(input('몸무게(kg) : '))
tallm = float(input('신장(m) : '))

bmi = weight / (tallm ** 2)

print(f'BMI : {bmi:.1f}')


# 문제 해결 5-5 홀짝 게임하기

coin = int(input('손 안에 동전 수를 입력하세요. : '))

if coin % 2 == 0:
    print(0)
else:
    print(1)


# 문제 해결 5-6 빵 나누기

bunbae = int(input('빵을 나누어 줄 수 있는 학생 수 : '))

# 빵 나누기
breads = 97
divsor = 3
studs = 97 // 3
mods = 97 % 3

print(f'''
빵을 나누어 줄 수 있는 학생 수: {studs}
남는 빵 갯수 : {mods}''')

# 전염병 예상 감염자 구하기
# 1일차 -> 2명
# 2일차 -> 4명
# 3일차 -> 8명
# 4일차 -> 16명
# n일차 -> 2 ** n명

infectors = 2 ** 30

print(f'30일 이후 예상 감염자 수 : {infectors}')
