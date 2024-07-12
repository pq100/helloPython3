# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 이름 : 홍길동, 국어: 99, 영어: 98, 수학 : 99
# 총점, 평균, 학점을 계산하고 출력함
# 단, 학생 3명에 대해 성적처리를 진행함

# 이름: 민지, 국어: 99, 영어: 98, 수학: 99
# 이름: 혜린, 국어: 88, 영어: 77, 수학: 66
# 이름: 다니엘, 국어: 55, 영어: 77, 수학: 99

# 성적 데이터 입력 받음
name1 = input('1번 학생 이름은? : ')
kor1 = int(input('1번 학생 국어는? : '))
eng1 = int(input('1번 학생 영어는? : '))
math1 = int(input('1번 학생 수학은? : '))

name2 = input('2번 학생 이름은? : ')
kor2 = int(input('2번 학생 국어는? : '))
eng2 = int(input('2번 학생 영어는? : '))
math2 = int(input('2번 학생 수학은? : '))

name3 = input('3번 학생 이름은? : ')
kor3 = int(input('3번 학생 국어는? : '))
eng3 = int(input('3번 학생 영어는? : '))
math3 = int(input('3번 학생 수학은? : '))

# 성적 처리
tot1 = kor1 + eng1 + math1
avg1 = tot1 / 3
# grd = '수' if (avg >= 90) else '우'
grd1 = '수' if (avg1 >= 90) else \
      '우' if (avg1 >= 80) else \
      '미' if (avg1 >= 70) else \
      '양' if (avg1 >= 60) else '가'

tot2 = kor2 + eng2 + math2
avg2 = tot2 / 3
# grd = '수' if (avg >= 90) else '우'
grd2 = '수' if (avg2 >= 90) else \
       '우' if (avg2 >= 80) else \
       '미' if (avg2 >= 70) else \
       '양' if (avg2 >= 60) else '가'

tot3 = kor3 + eng3 + math3
avg3 = tot3/ 3
# grd = '수' if (avg >= 90) else '우'
grd3 = '수' if (avg3 >= 90) else \
      '우' if (avg3 >= 80) else \
      '미' if (avg3 >= 70) else \
      '양' if (avg3 >= 60) else '가'

# 결과 출력
print(f'''이름: {name1}, 국어: {kor1}, 영어: {eng1}, 수학: {math1},
      총점: {tot1}, 평균: {avg1:.1f}, 학점: {grd1}''')

# 결과 출력
print(f'''이름: {name2}, 국어: {kor2}, 영어: {eng2}, 수학: {math2},
      총점: {tot1}, 평균: {avg1:.1f}, 학점: {grd1}''')

# 결과 출력
print(f'''이름: {name3}, 국어: {kor3}, 영어: {eng3}, 수학: {math3},
      총점: {tot3}, 평균: {avg3:.1f}, 학점: {grd3}''')
