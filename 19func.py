# 함수
# 특정 기능을 수행하는 코드블록(모음)에 이름을 부여한 것
# 즉, 여러 곳에 반복적으로 사용할 가치가 있는 코드들을
# 한 뭉치로 묶고 (어떤 값을 입력하면) 결과가 반환되도록
# 작성한 것 - 재사용이 주 목적
# 이 처럼 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악가능


print('오늘 날씨는 비옴!')     # 단순 출력

print('오늘 날씨는 비옴!')     # 반복 출력
print('오늘 날씨는 비옴!')
print('오늘 날씨는 비옴!')
print('오늘 날씨는 비옴!')

for _ in range(3):           # 개선된 반복
    print('오늘 날씨는 비옴!')

# 만약, 이러한 반복문을 여러번 반복해야 한다면 ?
# 또, '비옴' 대신 '맑음'이나 '흐림'으로 바꾸고 싶다면?
# => 함수를 이용!

# 함수 정의
# def 함수명(매개변수):
#     함수 몸체

def say_weather():
    for _ in range(3):
        print('오늘 날씨는 비옴!')

# 함수호출 1
# 함수명()

say_weather()

# 함수 정의 - 매개변수 선언
def say_weather(info):
    for _ in range(3):
        print(f'오늘 날씨는 {info}!')


# 함수 호출 2 - 함수명(인자)
say_weather('비옴')
say_weather('맑음')
say_weather('흐림')


# 단위 변환 : 인치 -> 센티미터
print(14 * 2.54)

def convert_inch(inch):
    cm = inch * 2.54
    print(f'{inch} -> {cm:.1f} cm')

inch = float(input(f'길이를 입력하세요(inch) : '))
convert_inch(inch)


# 변수의 유효 범위 scope
# scope : 변수가 접근 가능한 범위를 의미
# 전역 scope : 프로그램의 최상위 레벨에서 정의된 변수
#             어느 곳에서나 접근 가능
#             함수내에서 전역 변수로의 접근(사용) 가능
#             단, 전역 변수를 함수 내에서 수정 시 global이라는 키워드 필요!

# 지역 scope : 반복문 내부 / 함수 내부에 정의된 변수
#             반복문이나 함수 내에서만 접근 가능
#             반복문 실행 종료나 함수 호출이 끝나면 자동 소멸

x = 10      # 전역 변수
y = 10

def func():
    x = 20
    print('func : x = ', x)

def func2():
    global y           # 함수내에서 전역 변수를 제어하기 위해 global 선언
    y = 20
    print('func : y = ', y)
    
print(x)    # x 출력
func()      # X 변수가 있는 함수 호출
print(x)


print(y)
func2()
print(y)


# 웹 사이트 방문 횟수 누적 프로그램
visits = 0

isflag = False
while isflag:
    menu = input('1. 웹사이트 방문 2. 종료 : ')
    if menu == '1':
        visits += 1
        print(f'누적 방문 횟수', visits)
    else:
        print('방문을 종료합니다.')
        isflag = False

def count_visitor():
    global  visits
    visits += 1
    print('누적 방문 횟수 : ', visits)

# 누적 방문자 수 처리 함수 정의
isflag = True
while isflag:
    menu = input('1. 웹사이트 방문 2. 종료 : ')
    if menu == '1':
        count_visitor()
    else:
        print('방문을 종료합니다.')
        isflag = False

# -----------
goods = 1
goodscount = [5, 2, 10, 3]

def printReceipt():
    total = 0
    # total = 1000 * goodscount[0]  # 리스트는 참조(주소) 자료형이므로
                                    # 별다른 코드 없이 해당 변수 접근 가능
    print('total : ', total)

    goodscount[0] = 10              # 함수 내에서 global없이 리스트의 일부 변경 가능
    total2 = 1000 * goodscount[0]
    print('total2', total2)

    # goodscount = [99,99,99,99]    # 전역 변수 자체를 변경하려고 시도시 - 오류 발생! - global 필요!!

    print('goodscount[0] : ', goodscount[0])
    goodscount[0] = 10
    # print(goods)    # goods라는 변수가 없는데 호출해서 출력 시도 - 실패
                      # 선언 안된 변수를 호출해서 출력 시도 - 실패
    goods = 5         # goods 변수 선언 후 5라는 값 저장 - 성공

printReceipt()
print(goodscount[0])