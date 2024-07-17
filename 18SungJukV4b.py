# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 이름 : 홍길동, 국어: 99, 영어: 98, 수학 : 99
# 총점, 평균, 학점을 계산하고 출력함
# CRUD 기능을 지원하는 성적처리 프로그램으로 재작성하기 위해
# 즉, 성적 입력, 상세조회, 수정, 삭제 기능을 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 해당 명령 수행
# 학생 성적 데이터는 개별 변수가 아닌 리스트 안에 dict 형태로 저장


import sys

# 프로그램 메뉴 정의
main_menu = '''
================================
    성적 프로그램 v4b
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
sjs = []

# 메뉴 출력 및 메뉴별 처리
for i in range(100):
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('성적 데이터 추가')
        sj = {}
        sj['name'] = input('이름을 입력하세요: ')
        sj['kor'] = int(input('국어 점수를 입력하세요: '))
        sj['eng'] = int(input('영어 점수를 입력하세요: '))
        sj['mat'] = int(input('수학 점수를 입력하세요: '))
        sj['tot'] = sj['kor'] + sj['eng'] + sj['mat']
        sj['avg'] = sj['tot'] / 3
        grd = '수' if sj['avg'] >= 90 else \
            '우' if sj['avg'] >= 80 else \
                '미' if sj['avg'] >= 70 else \
                    '양' if sj['avg'] >= 60 else '가'
        sj['grd'] = grd
        sjs.append(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        for sj in sjs:
            print(f"이름: {sj['name']}, 국어: {sj['kor']}, 영어: {sj['eng']}, 수학: {sj['mat']}")

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
    else:
        print('메뉴를 잘못 선택하셨습니다!!')
