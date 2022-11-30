import gh
#python mysql connection

import mysql.connector as con
mycon=con.connect(host="localhost",user="root",passwd="harshit",database='railways')
if mycon.is_connected():
    print("="*163,end="")
    print("++INDIAN STAR RAILWAYS++",end="")
    print("="*47)
cur=mycon.cursor()

#creating database





#star code

import star1

#intro

print("INDIAN STAR RAILWAYS")
print("Making a way to secure journey.......")
print("                                                 WE WELCOME YOU TO OUR SITE.......")
print()
print("                                                KINDLY PLEASE PROCEED WITH LOGIN / SIGN UP:-")

#LOGIN/SIGN UP
while True:
    print("IF YOUR ACCOUNT ALREADY EXISTS     :    1. LOGIN")
    print()
    print("IF YOU WANT TO CREATE NEW ACCOUNT  :    2. SIGN UP ")
    print()
    a=int(input("ENTER YOUR PREFERENCE FROM THE ABOVE : "))
    print()
    if(a==1):
        cust_id1=input("=> ENTER YOUR USERNAME / ID :  ")
        print()
        cust_pass1=input("=> ENTER YOUR PASSWORD    :  ")
        query="select * from custrecords where cust_id=%s and pass=%s"
        final=(cust_id1,cust_pass1)
        cur.execute(query,final)
        j=0
        for i in cur:
            j=i
        if j==0:
            print("******INVALID PASSWORD / USERNAME******")
        else:
            print("___________________________________YOU ARE SUCCESSFULLY LOGGED IN........__________________________________         ")
            break
    elif(a==2):
        print("                                 SIGN UP                     ")  #SIGN UP
        print("KINDLY PLEASE PROVIDE THE DETAILS BELOW SUCH THAT NO OPTION IS LEFT BLANK !!!!!!!")
        print()
        print()
        cust_name=input("               ENTER YOUR NAME : ")
        print()
        while True:
            
         cust_id=input(  "              ENTER YOUR 4 LETTER USERNAME / ID: ")
         
            
         d="select * from custrecords where cust_id=%s" 
         cur.execute(d,(cust_id,))
         g=0
         for i in cur:
                g=i
            
         if g==0 and len(cust_id)==4:  # to check availability of username
                    break
         elif(len(cust_id)!=4):

             
                 print()
                 print(" **WORD LIMIT NOT FOLLOWED** ")
                 print()
                 
         else:
                    print()                
                    print("     ****Username exists**** ")
                    print()               
        
            
        
        print()
        while True:
            cust_ph_no=input("                ENTER YOUR 10 DIGIT PHONE NO. : ")#phone number check
            print()
            if len(str(cust_ph_no))!=10:
                print("****INVALID PHONE NUMBER(Digits limit not followed)****")
                print()
            else:
                break
            
        while True:
            
            cust_age=int(input("                ENTER YOUR AGE(**Kindly make sure you are above age 18) : "))
            print()
            if len(str(cust_age))==2 and cust_age>=18: #age restriction
                break
            else:
                print()
                print("*******AGE LIMIT NOT FOLLOWED********")
                print()
        while True:
            while True:
             cust_pass=input("                ENTER YOUR 4 LETTER PASSWORD : ")
             if(len(cust_pass)!=4):
                print()
                print("**YOUR PASSWORD DOES'NT MEET THE REQUIRED WORD LIMIT**") #password match condition
                print()
             else:  
                 break
            print() 
            cust_passr=input("                RE-ENTER THE CONFIRMED PASSWORD : ")
            print()
            if cust_passr!=cust_pass:
                print("YOUR PASSWORDS DOES NOT MATCH......PLEASE RE-ENTER YOUR PASSWORD")
                print()
            else:
                break
        cur.execute("insert into custrecords values(%s,%s,%s,%s,%s)",(cust_id,cust_name,cust_ph_no,cust_age,cust_passr))
        mycon.commit()
        print("____________________________________YOUR ACCOUNT IS SUCCESSFULLY CREATED______________________________________")
        #final details enter into the sql table 
    
        break
    #MAIN MENU 
print("                                               WELCOME TO INDIAN STAR RAILWAYS                                  ")
print()
print("________________________________________________________________________________________________________________")
print()
print("                                                  HOW CAN WE HELP???                                            ")
print("                                KINDLY CHOOSE YOUR PREFERENCE FROM THE OPTIONS BELOW TO CONTINUE.............")
print()
while True:
    print("    1. TICKET RESERVATION")
    print("    2. TICKET CANCELLATION")
    print("    3. RESERVATION ENQUIRY")
    
    print("    4. HELP !!")
    print("    5. EXIT")
    print()
    f=int(input("ENTER YOUR PREFERENCE FROM THE ABOVE OPTIONS : "))
    print()
    print("______________________________________________________________________________________________________________________")
    
    #TICKET RESERVATION
    
    if(f==1):
        
        print("                                    YOU HAVE SELECTED OPTION 1. TICKET RESERVATION")
        print()
        print("FOLLOWING ARE THE TYPES OF TICKETS AVAILABLE :-  ")
        print()
        print("1. SLEEPER A/C")                                        #types of seats
        print("2. NON-SLEEPER A/C")
        print("3. NORMAL SLEEPER")
        print("4. NORMAL NON-SLEEPER")
        print()
        t=int(input("ENTER YOUR PREFERENCE FROM ABOVE :"))
        tic_type=0
        if t==1:
            tic_type="SLEEPER A/C"
        elif t==2:
            tic_type="NON-SLEEPER A/C"
        elif t==3:
            tic_type="NORMAL SLEEPER "
        elif t==4:
            tic_type="NORMAL NON-SLEEPER "
        print()
        print()
        print("_______________________________________________________________________________________________________________________")
        print()
        print("                              KINDLY FILL THE DETAILS BELOW TO PROCEED RESERVATION !!")
        print()
        print()
        print("                             ENTER YOUR MODE OF YOUR TRAVEL :")
        print()
        print("1. ONE WAY")
        print("2. ROUND TRIP")
        mode=int(input("ENTER YOUR PREFERENCE: "))#TRAVELLING MODE
        import random
        price=random.randint(3000,5000)
        price1=0
        if mode==2:
            price1=price*2 #PRICE ALLOCATION
        else:
            price1=price
        import seats    #BOOKING SEATS( USING UPDATIONS)
        
        #TICKET DETAILS
        
        print()
        cust_name2=input("                ENTER YOUR FULL NAME : ")
        print() 
        while True:
            cust_id2=input("                ENTER YOUR USERNAME / LOGIN ID : ")
            print()
            d="select * from custrecords where cust_id=%s"
            cur.execute(d,(cust_id2,))
            g=0
            for i in cur:
                g=i
                                             #USERNAME CHECK(IF CORRECT THEN PROCEED) 
            if g==0:
                print()
                print("******INVALID ID*******")
                print()
                print("**ENTER YOUR CORRECT ID**")
                print()
            else:
                break
        while True:
            cust_adhaar2=int(input("                ENTER YOUR 12-DIGIT AADHAAR CARD NO. : "))
            print() 
            if(len(str(cust_adhaar2))==12):# AADHAAR CARD WORD LIMIT CHECK(12)
                     break
            else:
                print()
                print("INVALID(**YOUR AADHAAR CARD NO. DOES'NT MEET THE REQUIRED DIGIT LIMIT**) ")
                print()
        cust_train=input("                ENTER THE TRAIN NAME OF YOUR CHOICE : ")
        print()
        cust_dest=input("                ENTER YOUR NAME OF YOUR DESTINATION STATION : ")#TRAIN RELATED DETAILS
        print()
        cust_source=input("                ENTER NAME OF YOUR SOURCE STATION :")
        print()
        
        import random
        cust_pnr_no=random.randint(1000000000,9999999999)#GENERATION OF PNR NUMBER
        
        cust_date=input("                ENTER DATE OF DEPARTURE(In format yyyy-mm-dd): ")
        print()
        cur.execute("insert into tick_reserve values(%s,%s,%s,%s,%s)",(cust_id2,cust_name2,cust_adhaar2,cust_pnr_no,cust_train))
        mycon.commit()
        cur.execute("insert into train_info values(%s,%s,%s,%s,%s)",(cust_pnr_no,cust_dest,cust_source,cust_date,tic_type))
        mycon.commit()# DETAILS INSERTED INTO TABLE
        print()
        print()
        print(" AMOUNT PAYABLE :",price1) #FINAL PRICE
        print()
        print()                          
        print("                                                           YOUR TICKET IS SUCCESSFULLY BOOKED........")
        print()
        print("                                                     ______________________________")
        print("                                                     |YOUR PNR NO. IS : " ,end="" )
        print(cust_pnr_no,"|")
        print("                                                     ______________________________ ")
        print()
        print("________________________________________________________________________________________________________________")
        print()
#TICKED BOOKED 

        #TICKET CANCELLATION
        
    if(f==2):
        print()
        print("                                             YOU HAVE SELECTED OPTION 2.TICKET CANCELLATION ")
        print()
        print()
        while True:
            o=input("                -ENTER YOUR USERNAME / LOGIN ID : ")
            print()
            d="select * from tick_reserve where cust_id=%s" #USERNAME CHECK
            cur.execute(d,(o,))
            g=0
            for i in cur:
                g=i
            
            if g==0:
                    print()
                    print("******INVALID ID*******")
                    print()
                    print("*ENTER YOUR CORRECT ID")
                    print()
            else:
                    break
                
        
        while True:
            pnr=int(input("                -ENTER YOUR PNR NO. : "))
            d="select * from tick_reserve where pnrno=%s"
            cur.execute(d,(pnr,))
            g=0
            for i in cur:#PNR CHECK
                g=i
            
            if g==0:
                    print("******INVALID PNR NO.*******")
                    print()
                    
            else:
                    break
        print("YOUR DETAILS ARE PROCESSING......")
        a=input("                                    ARE YOU SURE TO CANCEL YOUR TICKET ? (YES / NO ):")
        if a=='YES' or a=='yes':
            p="delete from tick_reserve where cust_id=%s and pnrno=%s"
            cur.execute(p,(o,pnr))
            mycon.commit()
            q="delete from train_info where pnrno=%s"
            cur.execute(q,(pnr,))
            mycon.commit()
            print()
            print("                                      YOUR TICKET IS SUCCESSFULLY CANCELLED...........")
            print()
            print("                                      **ONLY 50 PERCENT OF THE TOTAL AMOUNT WILL BE REFUNDED**")
            print()
            print("________________________________________________________________________________________________________________")
            print()

            #RESERVATION ENQUIRY
    if(f==3):
        print("YOU HAVE SELECTED OPTION 3.RESERVATION ENQUIRY")
        print()
        print()
        print()
        while True:
            o=input("                ENTER YOUR USERNAME / LOGIN ID :")
            print("                                                                      ")
            d="select * from tick_reserve where cust_id=%s"
            cur.execute(d,(o,))
            g=0
            for i in cur:
                g=i
            
            if g==0:
                    print("******INVALID ID*******")
                    print("*ENTER YOUR CORRECT ID")
            else:
                    break
                
        
        while True:
            pnr=int(input("                ENTER YOUR PNR NO. :"))
            print("")
            
            d="select * from tick_reserve where pnrno=%s"
            cur.execute(d,(pnr,))
            g=0
            for i in cur:
                g=i
            
            if g==0:
                    print("******THERE IS NO SUCH RESERVATION WITH THIS PNR NO.*******")
                    print()
            else:
                    break
        print("YOUR DETAILS ARE PROCESSING......")
        print()
        print()
        print()
        q=["                #ID / USERNAME :", "                #NAME :" ,"                #AADHAAR CARD NO.:","                #PNR NO.:","                #TRAIN NAME:"]
        print("THE FOLLOWING ARE THE DETAILS OF YOUR RESERVED TICKET....................... ")
        s=("",)
              
        j="select * from tick_reserve where cust_id=%s and pnrno=%s"
        cur.execute(j,(o,pnr))
        g=0
        for i in cur:
                g=i
        for b in range(0,len(q)):
           print(q[b],g[b])
           print()
        n=["                #DESTINATION :","                #SOURCE STATION:","                #DATE OF DEPARTURE:","                #CLASS:"]
        j="select destination,source_station,dateofdeparture,class from train_info where pnrno=%s"
        cur.execute(j,(pnr,))
        g=0
        for i in cur:
                g=i
        for b in range(0,len(n)):
           print(n[b],g[b])
           print()
    if(f==4):#help
        print()
        print("                                     YOU HAVE SELECTED OPTION 4.HELP")
        print()
        print()
        print()
        print("                                                +==HOW CAN WE HELP YOU ??==+")
        print("          1.FORGOT PNR")
        
        print("          2. FOR FURTHER INFORMATION...........")
        print()
        print()
        a=int(input("ENTER YOUR CHOICE:"))
        if (a==1):
            while True:
             Q=input("                ENTER YOUR USERNAME / LOGIN ID : ")
             print()
             d="select * from tick_reserve where cust_id=%s"
             cur.execute(d,(Q,))
             g=0
             for i in cur:
                g=i
            
             if g==0:
                    print("******INVALID ID*******")
                    print("*ENTER YOUR CORRECT ID")
             else:
                    break
                
            while True:
             o=input("                ENTER YOUR TRAIN NAME: ")
             print()
             d="select * from tick_reserve where train_name=%s and cust_id=%s"
             cur.execute(d,(o,Q))
             g=0
             for i in cur:
                g=i
            
             if g==0:
                    print()
                    print("******INVALID*******")
                    print()
                    print("*ENTER YOUR CORRECT TRAIN NAME")
                    print()
             else:
                    break
            a="select pnrno from tick_reserve where train_name=%s and cust_id=%s"
            cur.execute(a,(Q,o))
            for i in cur:
                g=i
            print()    
            print("                            YOUR PNR NO. IS :",end="")
            print(g[3])
            print()
            print("________________________________________________________________________________________________________________")
            print()

        if(a==2):
            print()
            print("                #FOR PAYMENT RELATED ISSUES / ENQUIRY : CONTACT :- ")
            print()
            print("                    -EMAIL : indianstarrailways@gmail.com ")
            print()
            print("                #FOR OTHER ENQUIRIES...... : CONTACT OUR HELPLINE NO. : +91 84488 13349,+91 70429 22178")
            print() 
            print("_____________________________________WE WILL SURELY LOOK INTO YOUR MATTER_______________________________________")
            print()
    if(f==5):
        break
print("                          PLEASE PROVIDE FEEDBACK FOR THE SERVICES PROVIDED BY US.......")
print()
print(" 1.   *")
print()
print(" 2.  * *")
print()
print(" 3. * * *")
print()
print(" 4.* * * *")
print()
print()
s=input("                ENTER YOUR PREFERENCE :")
print()
if(s=="1" or s=="2"):
    print("                             WE WILL TRY TO IMPROVE OUR SERVICES.......")
    print("                             WE APOLOGIZE FOR THE INCONVENIENCE   ")
    print()
else:
    print("                               THANKS FOR YOUR FEEDBACK.........HOPE WE WILL CONTINUE TO SERVE YOU THE BEST")
    print()
print("THANKS FOR VISITING OUR WEBSITE...........HOPE YOUR JOURNEY WILL BE SAFE AND SECURE")

                 
            
            
           
                
    
    

   


 
