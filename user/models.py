from MySQLdb import connect
from MySQLdb.cursors import DictCursor
# from django.db import models

# Create your models here.

def insert(name, email, password, gender):
    conn = getconnection()
    cursor = conn.cursor()
    sql = '''
    insert
	    into user
    values (null, %s, %s, password(%s), %s, now())'''
    cursor.execute(sql, (name, email, password, gender))
    conn.commit()
    cursor.close()
    conn.close()

def fetchone(email, password):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    select no, name
    from user
    where email=%s
    and password=password(%s);
    '''
    cursor.execute(sql, (email, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def fetchonebyno(no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    select name, email, gender, password
      from user
     where no= (%s);
    '''
    cursor.execute(sql, str(no))
    result = cursor.fetchone()
    # 자원정리
    cursor.close()
    conn.close()

    return result

def updateuser(name, password, gender, no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    update user
	set name= %s, password=password(%s), gender= %s
    where no = (%s);
    '''
    cursor.execute(sql, (name, password, gender, str(no)))
    result = cursor.fetchone()
    conn.commit()
    # 자원정리
    cursor.close()
    conn.close()

    return result

def updateuserwd(name, gender, no):
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    update user
	set name= %s, gender= %s
    where no = (%s);
    '''
    cursor.execute(sql, (name, gender, str(no)))
    result = cursor.fetchone()
    conn.commit()
    # 자원정리
    cursor.close()
    conn.close()

    return result



def getconnection():
    return connect(user='mysite',
            password='mysite',
            host='192.168.1.139',
            port=3307,
            db='mysite',
            charset='utf8')