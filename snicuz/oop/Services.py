# 성적 서비스 클래스

from snicuz.oop.models import SungJuk, Employee
from snicuz.oop.dao import SungJukDA0 as sjdao
from snicuz.oop.dao import EmpDAO as empdao


class SungJukService:
    # 데코레이터 : 함수에 추가 기능을 구현할 때 사용
    @staticmethod # 정적static 메서드 : 객체화 없이 바로 사용 가능한 메서드
                  # 정적메서드로 정의된 함수는 self 매개변수 지정 x
                  # 호출방법 : 클래스명.함수명
    def display_menu():
        main_menu = '''
    =========================
        성적 프로그램 v8
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
    def modify_sungjuk():
        sjno = input('수정할 학생번호는? ')
        sj = sjdao.selectone_sungjuk(sjno)  # 단일 데이터 조회로 수정
        result = '수정할 데이터가 존재하지 않아요!'
        if sj:  # 수정할 데이터가 존재한다면
            sj = SungJukService.readagain_sungjuk(sj)  # 수정할 데이터 입력 받기
            cnt = sjdao.update_sungjuk(sj) # 수정된 데이터 업데이트
            result = f'{cnt} 건의 데이터 수정됨!'

        print(result)



    def readagain_sungjuk(sj):
        nsj = SungJuk(sj.name, None, None, None)
        nsj.kor = int(input(f'{sj.name} 학생의 새로운 국어는? ({sj.kor})'))
        nsj.eng = int(input(f'{sj.name} 학생의 새로운 영어는? ({sj.eng})'))
        nsj.mat = int(input(f'{sj.name} 학생의 새로운 수학는? ({sj.mat})'))
        SungJukService.compute_sungjuk(nsj)
        nsj.sjno = sj.sjno # nsj[7] - 학생 번호
        print(nsj)
        return nsj


    @staticmethod
    def remove_sungjuk():
        sjno = input('삭제할 성적 데이터 번호는?')
        cnt = sjdao.delete_sungjuk(sjno)
        result = f'{cnt} 데이터 삭제가 완료되었습니다.'
        print(result)

# -------------------------------------------------------------

# 사원 클래스
class EmpService:
    def display_menu(self):
        main_menu = '''
    =========================
       - 사원 관리 프로그램 -
    =========================
       1. 사원 데이터 추가
       2. 사원 데이터 조회
       3. 사원 데이터 상세조회
       4. 사원 데이터 수정
       5. 사원 데이터 삭제
       0. 사원 관리 프로그램 종료
    ========================= 
    '''
        print(main_menu, end='')
        menu = input('=> 메뉴를 선택하세요 : ')
        return menu

    @staticmethod
    def read_emp():
        empid = input('사원 번호는? ')
        fname = input('사원 이름은? ')
        lname = input('사원 성은? ')
        email = input('사원 이메일은? ')
        phone = input('사원 전화번호는? ')
        hdate = input('사원 입사일은? ')
        jobid = input('사원 직책은? ')
        sal = input('사원 급여는? ')
        comm = input('사원 수당은? (없으면 0) ')
        mgrid = input('사원 매니저 번호는? (없으면 0) ')
        deptid = input('사원 부서 번호는? (없으면 0) ')

        emp = Employee(empid, fname, lname, email, phone, hdate, jobid, sal, comm, mgrid, deptid)
        return emp


    @staticmethod
    def add_emp():
        emp = EmpService.read_emp()
        emp.comm = float(emp.comm) if emp.comm != '0' else None
        emp.mgrid = int(emp.mgrid) if emp.mgrid != '0' else None
        emp.deptid = int(emp.deptid) if emp.deptid != '0' else None
        cnt = EmpDAO.insert_emp(emp)
        print(f'{cnt} 건의 데이터가 추가됨!!')

    @staticmethod
    def show_emp():
        pass

    @staticmethod
    def showone_emp():
        pass

    @staticmethod
    def modify_emp():
        pass

    @staticmethod
    def remove_emp():
        pass

