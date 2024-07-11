# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 이름 : 홍길동, 국어: 99, 영어: 98, 수학 : 99
# 총점: 297, 평균: 99.9, 학점: 수


# 성적 데이터 입력 받음
name = input('이름 : ')
hangle = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
math = int(input('수학 점수 : '))

# 성적 처리
avg = hangle + eng + math
pung = avg / 3
# grd = '수' if (avg >= 90) else '우'
grd = '수' if (avg >= 90) else \
      '우' if (avg >= 80) else \
      '미' if (avg >= 70) else \
      '양' if (avg >= 60) else '가'

# 결과 출력
print(f'''이름: {name}, 국어: {hangle}, 영어: {eng}, 수학: {math},
      총점: {avg}, 평균: {pung:.1f}, 학점: {grd}''')
