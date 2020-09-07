desc user;

-- 조회
select * 
from user
where email='dooly@gmail.com'
and password=password('1234');


-- 회원가입
insert
	into user
values (null, '둘리', 'dooly@gmail.com', password('1234'), 'male', now());

-- login

-- 조회
select no, name
from user
where email='dooly@gmail.com'
and password=password('1234');

-- 회원정보 수정


