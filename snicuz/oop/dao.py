import sqlite3

from snicuz.oop.models import SungJuk


# 성적 DAO 클래스
class SungJukDA0:
    # 데이터베이스 연결객체와 커서 생성
    @staticmethod
    def _make_conn():
        conn = sqlite3.connect('db/python.db')
        cursor = conn.cursor()
        return conn, cursor


    # 데이터베이스 연결객체와 커서 종료
    @staticmethod
    def _dis_conn(conn, cursor):
        cursor.close()
        conn.close()


    @staticmethod
    def insert_sungjuk(sj):
        sql = 'insert into sungjuk (name, kor, eng, mat, tot, avg, grd) \
           values (?,?,?,?, ?,?,?)'
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


    def selectone_sungjuk(self):
        pass


    def update_sungjuk(self):
        pass


    def delete_sungjuk(self):
        pass