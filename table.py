import mysql.connector as sql

conn = sql.connect(host='localhost', user='root', passwd='aishusql', database='bank')

cur = conn.cursor()
cur.execute(
    'create table customer_details(acct_no int primary key,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>10),address varchar(125),cr_amt float )')
