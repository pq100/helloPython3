def readUnit():
    mm = int(input('길이(mm)를 입력하세요: '))
    return mm

def converUnit(mm):
    units = [mm]
    units.append(mm * 0.1)
    units.append(mm * 0.001)
    units.append(mm * 0.03937)
    units.append(mm * 0.003281)
    return units

def printUnits (units):
    print(f'''
    {units[0]}mm --> {units[1]} cm
    {units[0]}mm --> {units[2]} m
    {units[0]}mm --> {units[3]} inch
    {units[0]}mm --> {units[4]} ft
    ''')


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