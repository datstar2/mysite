from django.test import TestCase

# Create your tests here.


# 페이지 당 글의 갯수
#  SZLIST = 5 << PAGE 사이즈 잡기

# 표시할 페이지수(밑단에번호)
#  SZPAGE = 5  # /board/list?p=3

# total_count = 74

# page_count = round(74 / SZLIST)









'''
    select rownum as X.rnum, X.name, X.user_no, X.no, X.title, X.content, X.hit, date_format(X.reg_date,'%Y-%m-%d %h:%i:%s') as reg_date, X.g_no, X.o_no, X.depth 
    from
    (select rownum as rnum, A.name, A.user_no, A.no, A.title, A.content, A.hit, A.reg_date, A.g_no, A.o_no, A.depth
    from (
    select u.name, b.user_no, b.no, b.title, b.content, b.hit, b.reg_date, b.g_no, b.o_no, b.depth
    from board b, user u
    where b.user_no = u.no
    order by g_no desc, o_no asc, no asc) A
    whrere rownum <= 30) X
'''