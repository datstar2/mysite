from MySQLdb import connect
from MySQLdb.cursors import DictCursor
# from django.db import models

# Create your models here.

def fetchlist():
    conn = getconnection()
    cursor = conn.cursor(DictCursor)
    sql = '''
    select no, name, message, date_format(reg_time,'%Y-%m-%d %h:%i:%s')as reg_time 
    from guestbook 
    order by no desc;
    '''
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def insert(name, password, message):
    conn = getconnection()
    cursor = conn.cursor()
    sql = 'insert into guestbook values(null, %s, %s, now(), %s);'
    cursor.execute(sql, (name, password, message))
    conn.commit()
    cursor.close()
    conn.close()

def delete(no, password):
    conn = getconnection()
    cursor = conn.cursor()
    sql = 'delete from guestbook where no=(%s) and password=(%s)'
    cursor.execute(sql, (no, password))
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