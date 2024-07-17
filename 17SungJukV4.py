# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 이름 : 홍길동, 국어: 99, 영어: 98, 수학 : 99
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로 재작성하기 위해
# 즉, 성적 입력, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행

import sys

# 프로그램 메뉴 정의
main_menu = '''
================================
    성적 프로그램 v4
================================
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 성적 프로그램 종료
================================
'''

# 성적 데이터 관련 변수 선언
sjs = [ ['일지매',99,98,65,251,83.7,'우'] ]


# 성적 데이터 관련 변수 선 언
names = []
kors = []
engs = []
maths = []
tots = []
avgs = []
grds = []

# 메뉴 출럭 및 메뉴별 처리

for i in range(100):
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('성적 데이터 추가')
        sj = []
        cnt = len(sjs)
        sj.append(input(f'{cnt}번 학생 이름은? '))
        sj.append(int(input(f'{cnt}번 학생 국어는? : ')))
        sj.append(int(input(f'{cnt}번 학생 영어는? : ')))
        sj.append(int(input(f'{cnt}번 학생 수학은? : ')))
        # sj = ['윤지', 99, 98, 99]
        sj.append(sj[1] + sj[2] + sj[3])
        # sj = ['윤지', 99, 98, 99, 297]
        sj.append(sj[4] / 3)
        # sj = ['윤지', 99, 98, 99, 297, 98.9]
        grd = '수' if (sj[5] >= 90) else \
            '우' if (sj[5] >= 80) else \
                '미' if (sj[5] >= 70) else \
                    '양' if (sj[5] >= 60) else '가'
        sj.append(grd)
        # sj = ['윤지', 99, 98, 99, 297, 98.9, '수']
        # 입력 받은 성적 데이터를 리스트에 저장
        sjs.append(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        for sj in sjs:
            print(f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}')

    elif menu == '3':
        print('성적 데이터 상세조회')
        pass
    elif menu == '4':
        print('성적 데이터 수정')
        pass
    elif menu == '5':
        print('성적 데이터 삭제')
        pass
    elif menu == '0':
        print('성적 데이터 종료')
        sys.exit(0)
        pass
    else:
        print('메뉴를 잘못 선택하셨습니다!!')


