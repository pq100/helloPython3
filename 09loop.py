# 반복문
# 특정 문장 / 코드를 지정할 횟수 / 조건에 반복 실행하는 문장

# 간단한 메세지 한번 출력
print('Hello, Python!')
print('Hello, Python!')
print('Hello, Python!')

# 메세지를 수정한다면? - 번거로움!
print('Hello, cloud!')
print('Hello, cloud!')
print('Hello, cloud!')

# 만약, 반복문을 사용한다면?
# 반복의 용이성과 수정의 편리함을 제공

# 파이썬의 반복문
# for    : 지정한 횟수만큼 반복 수행
# while  : 지정한 조건만큼 반복 수행

# 횟수에 따른 반복 - for
# 반복횟수는 range() 함수로 유추가능 : 종료값-1 - 시작값
# for  카운트 변수 in range(시작값, 종료값-1, 간격):
#      반복할 문장


# range 함수
# 시작값, 종료값-1 사이의 연속된 정수 반환
print(1,2,3,4,5,6,7,8,9,10)

print(list(range(1,10 + 1)))
print(list(range(1,10 + 1, 2)))

# for 사용예
for i in range(1, 1 + 10):
# for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

for i in range(1, 3 + 1):        # st ~ end-1
    print(f'Hello, World!! {i}')

for i in range(3):               # 0 ~ end-1
    print(f'Hello, World!! {i}')

for _ in range(3):               # 카운트 변수 생략
    print(f'Hello, World!!')

# 1 ~ 100 사이 모든 정수 합을 구하고 출력

num = range(1, 101)
hap = sum(num)

print(hap)
# --- 문제 풀이 ---
sum = 0
for i in range(1, 100 + 1):
    sum = sum + i
print(sum)

# 1 ~ 100 사이 짝수의 합을 구하고 출력
sum = 0

for i in range(2, 100 + 1, 2):
    sum = sum + i

print(sum)




# 메일 발송
count = int(input('메일 발송 횟수를 입력하세요 : '))
for _ in range(count):
    print('메일 발송!')


# 3의 배수 출력하기
result = ''
for i in range(1, 10 + 1):
    result += f'num = {i}\n'
    if i % 3 == 0:
        result += f'3의 배수!!\n'
    print(result)


# 구구단 출력하기 (5단)
result = ''
gugu = 5
for i in range(1, 10):
    result += f'{gugu} × {i} = {gugu * i}\n'

print(result)


# 줄바꿈 없이 출력하기 (end = '')
for i in range(1, 10 + 1):
# print(i, end = '/')
    result += f'{i} '

print(result)


# for문을 이용해 1 ~ 100까지 정수 중 3과 7의 공배수와 최소 공배수를 출력
result = ''
baesu = 3, 7
for i in range(1 , 100 + 1):
    if i % 3 == 0 and i % 7 == 0:
        result += f'{i}: 3과 7의 공배수\n'
    # 최소 공배수 출력
    result += f'최소 공배수: {baesu}\n'

print(result)

# range함수 사용예
print(list(range(-10, 0, 1))) # 음수 순서대로 -10 -9 -8 -7 -6 ...
print(list(range(10, 0, -1))) # 양수 순서대로 10 9 8 7 6 ...

# 문자열을 for문에 사용하기
str = 'Hello, World'

for c in str:
    print(c, end =' ')

## 3 6 9 게임 만들기
# 1 ~ 10 : 3 6 9

# result = ''
#
# for i in range(1, 101):
#     if '3' in str(i) or '6' in str(i) or '9' in str(i):
#         if str(i).count('3') + str(i).count('6') + str(i).count('9') == 2:
#             result += '짝짝! '
#         else:
#             result += '짝! '
#     else:
#         result += f'{i} '
#
# print(result)

for i in range(1, 101):
    if i < 10:
        if i % 3 == 0:
            print(f'{i} 짝!')
        else:
            print(i)
    else:
        clap = ''
        fnum = i // 10
        lnum = i % 10

        if fnum % 3 == 0: clap += '짝! '
        if lnum % 3 == 0 and lnum != 0: clap += '짝!'
        print(f'{i} {clap}')


# 한빛역 3개 노선의 열차 구하기
trainA = 10
trainB = 25
trainC = 30

for min in range(1, 540 + 1):
    hour = min // 60
    min = min % 60

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


# 로그인 기능 만들기
passwd = input('관리자 암호를 입력하세요. ')
isLogin = False

for i in range(5):
#    if not isLogin == False:
    if not isLogin:
        passwd = input('관리자 암호를 입력하세요')

    if passwd == 'hanbitac':
        isLogin = True
        print('로그인 되었습니다!')
    else:
        print('암호를 다시 입력하세요!')

if not isLogin: print('로그인 실패! 횟수 초과!')

