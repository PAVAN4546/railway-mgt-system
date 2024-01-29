import mysql.connector
class PASSENGERS:
    def __init__(self):
        self.conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pavan@123',
        database='Railway1'
        )
    def insertdetails(self,pid,pname,age,m_no,gender):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO passengers VALUES({pid},'{pname}',{age},{m_no},'{gender}')")
        self.conn.commit()
        print("DATA HAS BEEN INSERTED SUCCESFULLY")

from passengers  import PASSENGERS
obj2=PASSENGERS()

pid=int(input("please enter pid:"))
pname=input("please enter pname:")
age=int(input("please enter age:"))
m_no=int(input("please enter mobile no:"))
gender=input("please enter gender:")
obj2.insertdetails(pid,pname,age,m_no,gender)
