import mysql.connector
class TRANSACTIONS:
    def __init__(self):
        self.conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pavan@123',
        database='Railway1'
        )
    def insertdetails(self,tid,pid,fare,p_mode):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES({tid},'{pid}','{fare}','{p_mode}')")
        self.conn.commit()
        print("DATA HAS BEEN INSERTED SUCCESFULLY")

from transactions  import TRANSACTIONS
obj3=TRANSACTIONS()

pid=int(input("please enter pid:"))
tid=int(input("please enter tid:"))
fare=int(input("please enter fare:"))
p_mode=input("please enter payment_mode:")
obj3.insertdetails(tid,pid,fare,p_mode)