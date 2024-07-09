# 실전예제 1

print ('아이디 및 비밀번호 확인')

name = '홍길동'
idd = 'abc123'
passwd = 'xyz987'
print (f'{name} 고객님의 아이디는 {idd} 비밀번호는 {passwd}입니다.')


# 실전예제 2
regdate = '3월30일'
persent = '45%'
happy = '좋음'
time1 = '오전 6시 30분'
tiem2 = '오후 7시 20분'
miter1 = '0.5m'
miter2 = '1.5m'
miter3 = '0.5m'

print (f'내일 날씨 예보입니다.\n 월요일인 {regdate} 아침 최저 기온은 -1도, 낮 최고 기온은 10도로 예보됐습니다.\n'
       f'비올 확률은 {persent}이고, 미세먼지는 {happy} 수준일 것으로 예상됩니다. \n'
       f'일출 시간은 {time1}이고, 일몰 시간은 {tiem2}입니다. \n'
       f'바다의 물결은 남해 앞바다 {miter1}, 동해 앞바다 {miter2}, 서해 앞바다 {miter3} 높이로 일겠습니다. \n'
       f'지금까지 {regdate} 월요일 날씨 예보였습니다.')


# 2영수증 예제
print ('영수증 계산서')
soju = input('소주 몇명 마셨나요? ')


# 3 변수로 사용 가능한 것: rate1 , TimeLimit, numberOfWindows , long(자바에선 불가능 파이썬에선 가능)
# 다른 건 안되는 이유 맨앞 숫자, 중간에 특수문자로 사용 불가능하다.


# 11 - 이름, 몸무게, 나이를 변수로 선언하고 초기화
name = '일지매'
weight = 45.5
age = 35

print(name, weight, age)

# 12 - 생년 월일 계산
# 연나이 계산 : 현재년도 - 태어난년도
# 만나이 : 현재년도 - 태어난년도, 생일 지나지 않음 (-1)
# 한국식 나이 : 현재년도 - 태어난년도 + 1
currentYear = int(input('현재년도는? '))
birthYear  = int(input('생일의 년도는? '))
myAge = currentYear - birthYear

print(f'''현재년도가 {currentYear}이고, 생일의 년도가 {birthYear}일 때,
나이는 {myAge} 입니다.''')

# 13

# print('7 x 1 = 7')
# print('7 x 2 = 14')
# print('7 x 3 = 21')
# print('7 x 4 = 28')
# print('7 x 5 = 35')
# print('7 x 6 = 42')
# print('7 x 7 = 49')
# print('7 x 8 = 56')
# print('7 x 9 = 63')

dan = 7
print(f'''
{dan} x 1 = {dan * 1}
{dan} x 2 = {dan * 2}
{dan} x 3 = {dan * 3}
{dan} x 4 = {dan * 4}
{dan} x 5 = {dan * 5}
{dan} x 6 = {dan * 6}
{dan} x 7 = {dan * 7}
{dan} x 8 = {dan * 8}
{dan} x 9 = {dan * 9}''')