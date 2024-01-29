#importing required modules----#insert,update,read,delete.
from train_details  import details
from train_capacity  import capacity
from routes import ROUTES
from book_tickets import BOOK_TICKETS
import numpy as np


print("-------------Welcome to Railway Management System---------------")
print("----------For Inserting the Data Enter -1--")
print("----------For Reading the Data Enter -2--")
print("----------For Updating the Data Enter -3--")
print("----------For Deleting the Data Enter -4--")

opr=int(input("Please Enter Your Operation: "))
if opr==1:
    #taking data
    print("------For inserting the data in traindetails press 1---")
    print("------For inserting the data in traincapacity press 2---")
    print("------For inserting the data in routes press 3---")
    print("------For booking a ticket press 4---")
    inopr=int(input("Please select an operation: "))
    if inopr==1:
        obj=details()
        tno=int(input("please enter train no:"))
        scr=input("please enter SOURCE station:")
        dtn=input("please enter DESTINATION station:")
        tname=input("please enter TRAIN_NAME:")
        obj.insertdetails(tno,scr,dtn,tname)
    if inopr==2:
        obj1=capacity()
        obj=details()
        obj.trainnofetch()
        tno=int(input("please enter train no:"))
        AC_1=int(input("please enter Capacity of Ac_1:"))
        AC_2=int(input("please enter Capacity of Ac_2:"))
        AC_3=int(input("please enter 1Capacity of Ac_3:"))
        SL=int(input("please enter Capacity of SL:"))
        GENERAL=int(input("please enter Capacity of GENERAL:"))
        obj1.insertdetails(tno,AC_1,AC_2,AC_3,SL,GENERAL)
    if inopr==3:
        obj4=ROUTES()
        obj=details()
        obj.trainroutesfetch()
        tno=int(input("please enter train no:"))
        stop1=input("please enter stop1 name:")
        stop2=input("please enter stop2 name:")
        stop3=input("please enter stop3 name:")
        stop4=input("please enter stop4 name:")
        obj4.insertdetails(tno,stop1,stop2,stop3,stop4)
    if inopr==4:

       obj1=BOOK_TICKETS()
       source_station=input('Enter source from above Station Names:')
       destination_station=input('Enter destination from above Station Names:')
       print(obj1.trainfetch(source_station,destination_station))
       trainno=int(input("Please enter Train no:"))
       obj=details()
       clas=input("Please enter your Coach:")

       #passenger info
       pid=int(input("Please enter your Id:"))
       pname=input("Please enter your Name:")
       age=int(input("Please enter your Age:"))
       gen=input("Please enter your Gender:")
       mno=int(input("Please enter your Mobile number:"))
       obj1.addpassenger(pid,pname,age,gen,mno)
       #making trasaction
       tid=int(input("Please enter Id:"))
       amount=int(input("Please enter Amount:"))
       mode=input("Please enter payment type:")
       obj1.addtransaction(tid,pid,amount,mode)
       #bookticket
       bid=np.random.randint(1,500000,1)[0]
       s_no=np.random.randint(1,50,1)[0]
       obj1.bookticket(bid,pid,clas,s_no,tid,source_station,destination_station,trainno)
if opr==2:
    pass
if opr==3:
    pass
if opr==4:
    pass








































