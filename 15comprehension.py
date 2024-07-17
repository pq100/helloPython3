# 컴프리헨션 comprehension - 반복문 축약
# 다양한 데이터 객체에 사용되는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능
# 퍼아썬에는 4가지 종류의 축약 지원
# list(py2) set, dict, generator (py3)

# 리스트에 적용하는 축약
# 1 ~ 10 까지의 정수를 리스트에 저장
a = list(range(1, 10+1))
print(a)

b = []
for i in range(1, 10+1):
    b.append(i)
print(b)

# list for 축약문
# [ 표현식 for 항목 in 반복 가능 객체]
c = [i for i in range(1, 10+1) ]
print(c)

# 1 ~ 10 사이 정수의 제곱값을 리스트로 생성하는 축약문
d = []
for i in range(1, 10+1):
    d.append(i * i)
print(d)

e = [ (i * i) for i in range(1, 10+1) ]
print(e)


# 다음 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 저장하는 예제
val1 = [1, 2, 3, 4, 5]
val2 = [1, 2, 'A', False, 9, 100]


f = []
for v in val1:
    f.append(v ** 2)
print(f)

g = []
for v in val2:
    if type(v) == int:
        g.append(v ** 2)
print(g)

# for if 축약문
# [ 표현식 for 항목 in 반복가능 객체 if 조건 ]
j = [ v ** 2 for v in val2 if type(v) == int ]
print(j)



# 1 ~ 100 사이 정수 중 짝수만 골라서 리스트에 저장
k = [ n for n in range(1, 100+1) if n % 2 == 0 ]
print(k)