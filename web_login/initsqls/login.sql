--增test01
delete from info where id=4
delete from users where id=4
insert into users(id,username,password) values(4,'test01',md5('123456'))
insert into info(id,name,gender) values(4,'测试一','男')
--增test02
delete from info where id=5
delete from users where id=5
insert into users(id,username,password) values(5,'test02',md5('123456'))
insert into info(id,name,gender) values(5,'测试二','女')
--增test03
delete from info where id=6
delete from users where id=6
insert into users(id,username,password) values(6,'test03',md5('123456'))
insert into info(id,name) values(6,'测试三')
--删test04
delete from info where id=(select id from users where username='test04')
delete from users where username='test04'
--增test05
delete from info where id=7
delete from users where id=7
insert into users(id,username,password) values(7,'test05',md5('123456'))
insert into info(id,name) values(7,'测试五')
--删test06
delete from info where id=(select id from users where username='test06')
delete from users where username='test06'