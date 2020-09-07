desc guestbook;

-- list
  select no,
	     name,
         message,
         date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date
    from guestbook
order by no desc;

-- add
insert into guestbook values(null, '둘리', '1234', '호이~', now());
insert into guestbook values(null, '마이콜', '1234', '라면은 구공탄에 끓여!', now());

-- delete
delete from guestbook where no=2 and password='1234';


select * from guestbook;
