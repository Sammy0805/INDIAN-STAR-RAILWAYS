import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="harshit")
cur=mycon.cursor()
x="show databases"
cur.execute(x)
h=False			
for dblist in cur:
    if("railways" in dblist):
        h=True
        
        break
if h==False:
     cur.execute("create database railways")
     
     cur.execute("use railways")
     mycon.commit()
     table1="create table custrecords(cust_id varchar(4) primary key,cust_name varchar(20),cust_tell bigint,age int,pass char(4))"
     cur.execute(table1)

     table2="create table train_info(pnrno bigint , destination varchar(20), source_station varchar(20), dateofdeparture date, class varchar(20))"
     cur.execute(table2)

     table3="create table tick_reserve(cust_id char(4), cust_name varchar(15), adharcardno bigint, pnrno bigint primary key, train_name varchar(20))"
     cur.execute(table3)

     table4="create table seats(confirmed_seats int,vacant_seats int)"
     cur.execute(table4)
     
     
