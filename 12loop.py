# While 문
# 조건을 만족을 할때까지 반복 수행 - 반복 횟수는 모름

# 변수 = 초기값
# while 조건식 :
#     반복할 문장
#     변수 증가/감소

## 1 ~ 10까지 정수 출력
# for i in range(1, 10 + 1):
#     print(i, end = ' ')
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

# 1 ~ 50 사이 정수 중 홀수만 출력
i = 1
while i <= 50:
    print(i, end='')
    i += 2

i = 1
while i <= 50:
    print(i, end='')
    i += 2

# 1 ~ 50 사이 정수 중 9의 배수만 출력
i = 1
while i <= 50:
    if i % 9 == 0:
        print(i, end=' ')
        i += 1

# 반복문 내 실행 중지 : break
# for, while 문 내에서 반복 흐름을 벗어나기 위해 사용


# 1 ~ 10000사이 정수의 합을 출력
# 단, 정수의 합이 12345678보다 계산을 중지
sum = 0

for i in range(1, 10000 + 1):
    if sum > 12345678: break
    sum += i

print(sum)

# 1 ~ 10000사이 정수의 합을 출력
# 단, 정수의 합이 12345678보다 계산을 중지 (while 문으로 작성)
i = 1
sum = 0
while i < 10001:
    if sum > 12345678: break
    sum += i
    i += 1

print(sum, i)


# while 문을 이용해 1 ~ 100까지 정수 중 3과 8의 공배수와 최소 공배수를 출력

# 1 ~ 100까지 정수 중 3과 8의 공배수와 최소 공배수를 출력
result = ''

for i in range(1, 100+1):
    if i % 3 == 0 and i % 8 ==0:
        result += f'{i} '

print(result, f'[{3 * 8}]')



# 삼각형의 넓이 구하기
limitArea = 150     # 반복 중단 삼각형 너비
width = 2
height = 3
i = 1

while True:
    area = ((width * i) * (height * i)) / 2
    if area > limitArea: break
    print(f'삼각형 너비 : {width * i} / {height * i} = {area}')
    i += 1



## 3 6 9 게임 만들기 (while문으로 작성)
# 값 in str(문자열)
# '3' in str(36)
# '6' in str(36)
# '9' in str(12)
i = 1
while i < 100:
    jjak = ''
    if '3' in str(i): jjak += ' 짝!'
    if '6' in str(i): jjak += ' 짝!'
    if '9' in str(i): jjak += ' 짝!'
    if i == 33 or i == 66 or i == 99: jjak += ' 짝!'
    print(i, jjak)
    i += 1


# 열차 교차시간 알아보기
trainA = 10
trainB = 25
trainC = 30
min = 1


# for min in range(1, 540 + 1):  <<< 이게 밑의 while문과 같음

while min < 541:
    # if 문들

    if min % trainA == 0 and min % 25 == 0:  # 10분 간격
        print(f'{hour}시 {min}분 : A - B 교차!')

    elif min % trainB == 0 and min % trainC == 0: # 50분 간격
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : B - C 교차!')

    elif min % trainC == 0 and min % trainA == 0: # 30분 간격
        hour = 9 + min // 60
        min = min % 60
        print(f'{hour}시 {min}분 : C - A 교차!')

    min += 1


# 로그인 기능 만들기
cntLogin = 1

while True:
    passwd = input('관리자 암호를 입력하세요. ')

    if passwd == 'hanbitac':
        isLogin = True
        print('로그인 되었습니다!')
        break
    else:
        print('암호를 다시 입력하세요!')

    if cntLogin < 5: cntLogin += 1
    else:
        print('로그인 실패! 횟수 초과!')
        break

