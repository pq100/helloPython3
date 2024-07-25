# import sqlite3
import pymysql

from snicuz.oop.models import SungJuk, Employee

host='13.208.165.126'
user='clouds2024'
passwd='clouds2024'
dbname='clouds2024'


# 성적 DAO 클래스
class SungJukDA0:
    # 데이터베이스 연결객체와 커서 생성
    @staticmethod
    def _make_conn():
        conn = pymysql.connect(host=host, user=user, password=passwd, database=dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor


    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn, cursor):
        cursor.close()
        conn.close()


    @staticmethod
    def insert_sungjuk(sj):
        """
        입력한 성적 데이터를 sungjuk 테이블에 저장
        :param sj: 테이블에 저장할 성적 데이터
        :return cnt: 테이블에 성공적으로 저장된 데이터 건수
        """
        sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd) \
           values (%s,%s,%s,%s, %s,%s,%s)'
        conn, cursor = SungJukDA0._make_conn()
        params = (sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDA0._dis_conn(conn, cursor)
        return cnt



    @staticmethod
    def select_sungjuk():
        sjs = []
        sql = 'select sjno,name,kor,eng,mat,substr(regdate,0,11) regdate from sungjuk'
        conn, cursor = SungJukDA0._make_conn()
        cursor.execute(sql)

        rs = cursor.fetchall()
        for r in rs:        # 조회 결과를 SungJuk 객체에 개별 저장
            sj = SungJuk(r[1], r[2], r[3], r[4])
            sj.sjno = r[0]
            sj.regdat = r[5]
            sjs.append(sj)

        SungJukDA0._dis_conn(conn, cursor)
        return sjs


    def selectone_sungjuk(sjno):
        sql = 'select * from sungjuk where sjno = %s'
        conn, cursor = SungJukDA0._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        rs = cursor.fetchone()
        if rs:
            sj = SungJuk(rs[1], rs[2], rs[3], rs[4])
            sj.sjno = rs[0]
            sj.tot = rs[5]
            sj.avg = rs[6]
            sj.grd = rs[7]
            sj.regdate = rs[8]
        else:
            sj = None

        SungJukDA0._dis_conn(conn, cursor)
        return sj



    @staticmethod
    def update_sungjuk(sj):
        sql = 'update sungjuk set kor=%s, eng=%s, mat=%s, tot=%s, avg=%s, grd=%s \
               where sjno = %s'
        conn, cursor = SungJukDA0._make_conn()
        cursor = conn.cursor()
        params = (sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sj.sjno)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDA0._dis_conn(conn, cursor)
        return cnt


    @staticmethod
    def delete_sungjuk(sjno):
        sql = 'delete from sungjuk where sjno = %s'
        conn, cursor = SungJukDA0._make_conn()
        params = (sjno,)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        SungJukDA0._dis_conn(conn, cursor)
        return cnt

#----------------------------------------------------------------------------------------------------
# 사원 DAO 클래스
class EmpDAO:
    # 데이터베이스 연결객체와 커서 생성
    @staticmethod
    def _make_conn():
        conn = pymysql.connect(host=host, user=user,
                               password=passwd, database=dbname, charset='utf8')
        cursor = conn.cursor()
        return conn, cursor

    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn,cursor):
        cursor.close()
        conn.close()

    # 사원 데이터 저장
    @staticmethod
    def insert_emp(emp):
        sql = "insert into emp values " \
              "(%s,%s,%s,%s, %s,%s,%s,%s, %s,%s,%s)"
        conn, cursor = EmpDAO._make_conn()
        params = (emp.empid,emp.fname,emp.lname,emp.email,
                  emp.phone,emp.hdate,emp.jobid,
                  emp.sal,emp.comm,emp.mgrid,emp.deptid)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        EmpDAO._dis_conn(conn, cursor)
        return cnt

    @staticmethod
    def select_emp():
        emps = []
        sql = 'select empid,fname,email,jobid,deptid from emp'
        conn,cursor = EmpDAO._make_conn()
        cursor.execute(sql)
        rs = cursor.fetchall()
        for r in rs:
            emp = Employee(r[0], r[1], None, r[2],
                           None, None, r[3],
                           None, None, None, r[4])
            emps.append(emp)

        EmpDAO._dis_conn(conn, cursor)
        return emps

    @staticmethod
    def selectone_emp(empid):
        sql = 'select * from emp where empid = %s'
        conn, cursor = EmpDAO._make_conn()
        params = (empid,)
        cursor.execute(sql, params)
        rs = cursor.fetchone()
        if rs:
            emp = Employee(rs[0],rs[1],rs[2],rs[3],rs[4],rs[5],
                           rs[6],rs[7],rs[8],rs[9],rs[10])
        else:
            emp = None

        EmpDAO._dis_conn(conn, cursor)
        return emp

    @staticmethod
    def delete_emp(empid):
        sql = "delete from emp where empid = %s"
        conn, cursor = EmpDAO._make_conn()
        params = (empid,)
        cursor.execute(sql, params)
        cnt = cursor.rowcount
        conn.commit()
        EmpDAO._dis_conn(conn, cursor)
        return cnt