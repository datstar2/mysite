from MySQLdb import connect
from MySQLdb.cursors import DictCursor
# from django.db import models

# Create your models here.

def fetchlist():
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    select u.name, b.user_no, b.no, b.title, b.content, b.hit, date_format(b.reg_date,'%Y-%m-%d %h:%i:%s')as reg_date, b.g_no, b.o_no, b.depth
    from board b, user u
    where b.user_no = u.no
    order by g_no desc, o_no asc, no asc;
    '''
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def fetchonebyno(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    select no, title, content
      from board
     where no= %s;
    '''
    cursor.execute(sql, [no])
    result = cursor.fetchone()
    # 자원정리
    cursor.close()
    conn.close()
    return result

def fetchonebynore(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    select no, g_no, o_no, depth
      from board
     where no= %s;
    '''
    cursor.execute(sql, [no])
    result = cursor.fetchone()
    # 자원정리
    cursor.close()
    conn.close()
    return result

def insert(title, content, user_no):
    conn = getconnection()
    cursor = conn.cursor()
    sql = 'insert into board values(null, %s, %s, 0, now(), 0, 0, 0,%s);'
    cursor.execute(sql, (title, content, user_no))
    conn.commit()
    cursor.close()
    conn.close()

def updateboard(title, content, no):
     conn = getconnection()
     cursor = conn.cursor(DictCursor)
     sql = '''
    update board
	set title= %s, content= %s
     where no = %s;
        '''
     cursor.execute(sql, (title, content, no))
     result = cursor.fetchone()
     conn.commit()
     # 자원정리
     cursor.close()
     conn.close()

     return result

def updatereply(g_no, o_no, depth, no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
        update board
    	set g_no = %s, o_no = %s, depth = %s
         where no = %s;
            '''
    cursor.execute(sql, [g_no, o_no, depth, no])
    result = cursor.fetchone()
    conn.commit()
    # 자원정리
    cursor.close()
    conn.close()

    return result

def hitplus(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
        update board
    	set hit = hit+1
         where no = %s;
            '''
    cursor.execute(sql, [no])
    result = cursor.fetchone()
    conn.commit()
    # 자원정리
    cursor.close()
    conn.close()

    return result

def g_noplus(gno, no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
        update board
    	set g_no = %s + 1
         where no = %s;
            '''
    cursor.execute(sql, [gno, no])
    result = cursor.fetchone()
    conn.commit()
    # 자원정리
    cursor.close()
    conn.close()
    return result

def maxno():
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = "select MAX(no) from board"
    cursor.execute(sql)
    ndict = cursor.fetchone()
    print(ndict)
    conn.commit()
    cursor.close()
    conn.close()
    return ndict.get('MAX(no)')

def maxg_no():
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = "select MAX(g_no) from board"
    cursor.execute(sql)
    ndict = cursor.fetchone()
    print(ndict)
    conn.commit()
    cursor.close()
    conn.close()
    return ndict.get('MAX(g_no)')

def neworder(g_no, o_no, no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
        update board
    	set o_no = o_no+1
         where g_no = %s
          and o_no >= %s
          and  no != %s 
            '''
    cursor.execute(sql, [g_no, o_no, no])
    result = cursor.fetchone()
    conn.commit()
    # 자원정리
    cursor.close()
    conn.close()
    return result

def delete(no):
    conn = getconnection()
    cursor = conn.cursor()
    sql = 'delete from board where no = %s'
    cursor.execute(sql, [no])
    conn.commit()
    cursor.close()
    conn.close()

def getconnection():
    return connect(user='mysite',
            password='mysite',
            host='192.168.1.139',
            port=3307,
            db='mysite',
            charset='utf8')