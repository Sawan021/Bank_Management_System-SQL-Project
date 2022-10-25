import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='aishusql',database='bank')
cur = conn.cursor()
cur.execute('create table transactions(acct_no int(50),date date ,withdrawal_amt bigint(20),amount_added bigint(20) )')