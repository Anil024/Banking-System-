import mysql.connector
import datetime
from datetime import datetime
datetime_obj = datetime.now()
# extract the time from datetime_obj
date = datetime_obj.date()
con=mysql.connector.connect(host='localhost',user='root',password='',database='pythondb')
cur=con.cursor()
print("press 1 to create new Account")
print("press 2 to withdrow the Money")
print("press 3 to Deposite the Money")
print("press 4 for Fund Transfer")
print("press 5 to Show Balance")
print("press 6 Change Pin Number")
print("press 7 to Print Account Summary")

n=int(input("Enter Your Choice "))
if n==1:
    ac="SBI"
    Q="select * from account "
    cur.execute(Q)
    x=0
    for row in cur:
        x=x+1
    if x>0:
        x=x+1
        ac=ac+str(x)
    else:
        ac="SBI101"
    pin=input("enter pin number")
    name=input("enter your Name")
    fname=input("Enter First Name")
    gender=input("enter Your Gender M or F")
    email=input("enter your email")
    phone=input("enter your conatact number")
    state=input("enter State Name")
    city=input("enter City Name")
    amount=int(input("enter amount with you want to open"))
    s="insert  into account(Acno,Pin,Name,Fname,Gender,Email,Phone,State,City,Amount)values('"+ac+"','"+pin+"','"+name+"','"+fname+"','"+gender+"','"+email+"','"+phone+"','"+state+"','"+city+"','"+str(amount)+"')"
    cur.execute(s)
    con.commit()
    print("Account Created Successfully")

if n==2:
    ac=input("Please enter your account n.")
    pin=input("enter your pin number")
    s="select * from account where acno='"+ac+"' and Pin='"+pin+"'"
    cur.execute(s)
    x=0
    camt=0
    for row in cur:
        x=x+1
        camt=int(row[9])
    if x>0:
        wamt=int(input("Enter Amount to withdraw"))
        if camt>=wamt:
            camt=camt-wamt
            q=1
            q="update account set Amount='"+str(camt)+"' where acno='"+ac+"'"
            cur.execute(q)
            con.commit()
            print("After withdraw ",wamt," YOur Current balande is = ",camt)

            #  code for transation table
            ds="Withdraw"
            tc=1
            q1="insert into trans(acno,dt,amt,ds)values('"+ac+"','"+str(date)+"','"+str(wamt)+"','witdraw')"
            cur.execute(q1)
            con.commit()
        else:
            print("Insufficient balance")
    else:
        print("Invlaid Accoutn or Pin")

if n==3:
    ac=input("Please enter your account n.")
    pin=input("enter your pin number")
    s="select * from account where acno='"+ac+"' and Pin='"+pin+"'"
    cur.execute(s)
    x=0
    camt=0
    for row in cur:
        x=x+1
        camt=int(row[9])
    if x>0:
        print("your account balance is ",camt)
        damt=int(input("enter amount to deposit"))
        camt=camt+damt
        q="update account set Amount='"+str(camt)+"' where acno='"+ac+"'"
        cur.execute(q)
        con.commit()
        print("Amount Added Scuccessfuly")
        print("your current Balance is ",camt)
        # code for transaction
        q1="insert into trans(acno,dt,amt,ds)values('"+ac+"','"+str(date)+"','"+str(damt)+"','diposite')"
        cur.execute(q1)
        con.commit()

    else:
        print("Invalide Credential ")  

if n==4:
    ac=input("Please enter your account n.")
    pin=input("enter your pin number")
    s="select * from account where acno='"+ac+"' and Pin='"+pin+"'"
    cur.execute(s)
    x=0
    camt=0
    for row in cur:
        x=x+1
        camt=int(row[9])
    if x>0:
        tamt=int(input("Enter Amount to withdraw"))
        if camt>=tamt:
            ac2=input("enter the account n. to transfer")
            s="select * from account where acno='"+ac2+"'"
            cur.execute(s)
            x=0
            camt2=0
            for row in cur:
                x=x+1
                camt2=int(row[9])
            if x>0:
                camt=camt-tamt
                camt2=camt2+tamt
                q="update account set Amount='"+str(camt)+"' where acno='"+ac+"'"
                cur.execute(q)
                con.commit()
                # code for transaction table
                q1="insert into trans(acno,dt,amt,ds)values('"+ac+"','"+str(date)+"','"+str(tamt)+"','transfer')"
                cur.execute(q1)
                con.commit()
                q="update account set Amount='"+str(camt2)+"' where acno='"+ac2+"'"
                cur.execute(q)
                con.commit()
                # code for transaction table
                q1="insert into trans(acno,dt,amt,ds)values('"+ac2+"','"+str(date)+"','"+str(tamt)+"','recieved')"
                cur.execute(q1)
                con.commit()
                print("After Transfer ",tamt," Your Current balance is = ",camt)
            else:
                print("invalide Benificary Account N.")   
            
        else:
            print("Insufficient balance")
    else:
        print("Invlaid Accoutn or Pin")

if n==5:
    ac=input("enter account n.")
    s="select * from account where acno='"+ac+"'"
    cur.execute(s)
    x=0
    camt=0
    for row in cur:
        x=x+1
        camt=int(row[9])
    if x>0:
        print("your Account balance is ",camt)
    else:
        print("Invalide Credential")

if n==6:
    ac=input("enter your account n.")
    s="select * from account where acno='"+ac+"'"
    cur.execute(s)
    x=0
    pass1=""
    for row in cur:
        x=x+1
        pass1=row[1]
    if x>0:
        pass2=input("enter your previous password pin")
        if pass2==pass1:
            pin=input("enter new pin")
            s="update account set Pin='"+pin+"' where acno='"+ac+"'"
            cur.execute(s)
            con.commit()
            print("PAssword Pin Reset Successfully ")
        else:
            print("Wrong password enter ")

if n==7:
    ac=input("Please enter your account n.")
    pin=input("enter your pin number")
    s="select * from account where acno='"+ac+"' and Pin='"+pin+"'"
    cur.execute(s)
    x=0
    for row in cur:
        x=x+1
        
    if x>0:
        q1="select * from trans where acno='"+ac+"'"
        cur.execute(q1)
        m=0
        for row in cur:
        
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
        

    else:
        print("Invalid Credential")





 




   

