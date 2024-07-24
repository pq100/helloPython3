# 사원 등록 프로그램


import sys
from snicuz.oop.services import EmpService as empsrv



# 메뉴 출력 및 메뉴별 처리
while True:
    # 메뉴 입력 받음
    menu = empsrv.displayMenu()

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('사원 데이터 추가')
        empsrv.add_emp()

    elif menu == '2':
        print('사원 데이터 조회')
        empsrv.show_emp()

    elif menu == '3':
        print('사원 데이터 상세조회')
        empsrv.showOne_emp()

    elif menu == '4':
        print('사원 데이터 수정')
        empsrv.modify_emp()

    elif menu == '5':
        print('사원 데이터 삭제')
        empsrv.remove_emp()

    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')


