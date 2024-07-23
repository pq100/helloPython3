# 성적 서비스 클래스

from snicuz.oop.models import SungJuk
from snicuz.oop.dao import SungJukDA0 as sjdao
class SungJukService:
    # 데코레이터 : 함수에 추가 기능을 구현할 때 사용
    @staticmethod # 정적static 메서드 : 객체화 없이 바로 사용 가능한 메서드
                  # 정적메서드로 정의된 함수는 self 매개변수 지정 x
                  # 호출방법 : 클래스명.함수명
    def display_menu():
        main_menu = '''
    =========================
        성적 프로그램 v7b
    =========================
       1. 성적 데이터 추가
       2. 성적 데이터 조회
       3. 성적 데이터 상세조회
       4. 성적 데이터 수정
       5. 성적 데이터 삭제
       0. 성적 프로그램 종료
    ========================= 
    '''
        print(main_menu, end='')
        menu = input('=> 메뉴를 선택하세요 : ')
        return menu


    @staticmethod
    def read_sungjuk():
        name = (input(f'새로운 학생 이름은? '))
        kor = (int(input(f'새로운 학생 국어는? ')))
        eng = (int(input(f'새로운 학생 영어는? ')))
        mat = (int(input(f'새로운 학생 수학은? ')))
        return SungJuk(name, kor, eng, mat)



    @staticmethod
    def add_sungjuk():
        sj = SungJukService.read_sungjuk()
        SungJukService.compute_sungjuk(sj)
        cnt = sjdao.insert_sungjuk(sj)
        result = f'{cnt} 건의 데이터 추가 성공!!'
        print(result)


    @staticmethod
    def compute_sungjuk(sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        sj.grd = '가'
        if (sj.avg >= 90): sj.grd = '수'
        elif (sj.avg >= 80): sj.grd ='우'
        elif (sj.avg >= 70): sj.grd ='미'
        elif (sj.avg >= 60): sj.grd ='양'


    @staticmethod
    def show_sungjuk():
        result = ''
        sjs = sjdao.select_sungjuk()
        for sj in sjs:
            result += f'번호: {sj.sjno}, 이름: {sj.name}, 국어: {sj.kor}, 영어: {sj.eng}, 수학: {sj.mat}, 등록일: {sj.regdate}\n'
        print(result)


    @staticmethod
    def showone_sungjuk():
        sjno = input('조회할 학생 번호는? ')
        result = '데이터가 존재하지 않아요!!'
        sj = sjdao.selectone_sungjuk(sjno)
        if sj:   # 조회한 데이터가 존재한다면
            result = (f'번호: {sj.sjno}, 이름: {sj.name}, 국어: {sj.kor}, 영어: {sj.eng}, 수학: {sj.mat}\n'
                      f'총점: {sj.tot}, 평균: {sj.avg:.1f}, 학점: {sj.grd}, 등록일: {sj.regdate}')
        print(result)

    @staticmethod
    def modify_sungjuk(self):
        pass


    def readagain_sungjuk(self):
        pass


    @staticmethod
    def remove_sungjuk(self):
        pass