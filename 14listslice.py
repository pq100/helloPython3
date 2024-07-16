# 슬라이싱(slicing)
# 연속적인 객체들(리스트, 튜플, 문자열)에 범위를 지정하고
# 선택해서 부분벅으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 시퀀스 자료형에 지원되는 기능(순서를 기억함) 중에 하나
# 객체명[시작 :끝-1: 스텝]

# 슬라이싱 예제
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(alpha[2:5+1])
print(alpha[0:4+1], alpha[:4+1])
print(alpha[3:7+1])
print(alpha[5:9+1], alpha[5:])
print(alpha[3:8+1])

print(alpha[:])
print(alpha[::2])
print(alpha[::-1])    # 역방향

# 주민번호에서 생년월일과 성별코드 추출
# 문자열 슬라이스
jumin = '123456-1234567'

birth = jumin[:5+1]
gender = jumin[7:8]

print(birth)
print(gender)