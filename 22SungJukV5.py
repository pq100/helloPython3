import sys
import snicuz.sungjukv5 as sjv5

# 메뉴 출력 및 메뉴별 처리

while True:
    # 메뉴
    menu = sjv5.displayMenu()

    # 선택한 메뉴에 따라 해당 기능 수행
    if menu == '1':
        print('성적 데이터 추가')
        sj = sjv5.readSungJuk()
        sjv5.addSungJuk(sj)

    elif menu == '2':
        print('성적 데이터 조회')
        sjv5.showSungJuk()

    elif menu == '3':
        print('성적 데이터 상세조회')

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



