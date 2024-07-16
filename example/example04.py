# 51번 문제 구구단

print('''
Multiplication Table
    1   2   3   4   5   6   7   8   9
--------------------------------------
1 | 1   2   3   4   6   7   8   8   9
2 | 2   4   6   8   10  12  14  16  18
3 | 3   6   9   12  15  18  21  24  27
4 | 4   8   12  16  20  24  28  32  36
5 | 5   10  15  20  25  30  35  40  45
6 | 6   12  18  24  30  36  42  48  54
7 | 7   14  21  28  35  42  49  56  63
8 | 8   16  24  32  40  48  56  64  72
9 | 9   18  27  36  45  56  63  72  81
''', end='')

for i in range(1, 9+1):
    print(f'{i} |', end='')
    for j in range(1, 9+1):
        print(f'{i * j:4d}', end='')
print()




#
cardno = input('카드 번호는? ')
result = '잘못된 카드 번호입니다.'

if cardno[:2] == '35':
    if cardno == '356317':
        result = 'JCB카드 NH농협카드'
    elif cardno == '356901':
        result = 'JCB카드 신한카드'
    elif cardno == '356912':
        result = 'JCB카드 KB국민카드'

elif cardno[:1] == '4':
    if cardno == '404825':
        result = '비자카드 비씨카드'
    elif cardno == '438676':
        result = '비자카드 신한카드'
    elif cardno == '404825':
        result = '비자카드 KB국민카드'

elif cardno[:1] == '5':
    if cardno == '515594':
        result = '마스터카드 신한카드'
    elif cardno == '524353':
        result = '마스터카드 외한카드'
    elif cardno == '540926':
        result = '마스터카드 KB국민카드'

print(f'{cardno} / {result}')





