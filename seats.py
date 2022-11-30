import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="harshit",database="railways")
cur=mycon.cursor()
while True:
    conf_tick=int(input("NO. OF SEATS :"))
    vac_tick=100-conf_tick
    cur.execute("select vacant_seats from seats")
    c=cur.fetchall()
    



    
    cur.execute("select confirmed_seats from seats ")

    seat=cur.fetchall()
    
    if seat==[]:
        cur.execute("insert into seats values(%s,%s)",(conf_tick,vac_tick))
        mycon.commit()
        print("  **SEATS AVAILABLE** ")
        break
        
    else:
        #if seats are not available
        if (c[0][0]-conf_tick)<=0:
            print()
            print("**SEATS UNAVAILABLE**")
            print()
            print("VACANT SEATS ARE :",end="")
            print(c[0][0])
            continue
        else:
        #if seats are available
            updatetick="update seats set confirmed_seats=confirmed_seats+"+str(conf_tick)
            cur.execute(updatetick)
            mycon.commit()
            tick1="update seats set vacant_seats=vacant_seats-"+str(conf_tick)
            cur.execute(tick1)
            mycon.commit()
            print()
            print("**TICKETS AVAILABLE**")
            print()
            break
               
