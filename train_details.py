import mysql.connector
'''conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pavan@123',
        database='Railway1'
        )
        #limit , offset'''

class details:
    def __init__(self):
        self.conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pavan@123',
        database='Railway1'
        )
    def insertdetails(self,tno,scr,dtn,tname):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRAIN_DETAILS VALUES({tno},'{scr}','{dtn}','{tname}')")
        self.conn.commit()
        print("DATA HAS BEEN INSERTED SUCCESFULLY")
    def trainnofetch(self):
        self.cur=self.conn.cursor()
        self.cur.execute("select train_details.train_no from train_details left join train_capacity on train_details.train_no=train_capacity.train_no where ac_1 is null")
        print(self.cur.fetchall())
    def trainroutesfetch(self):
        self.cur=self.conn.cursor()
        self.cur.execute("select train_details.train_no,train_details.SOURCE,train_details.DESTINATION from train_details left join ROUTES on train_details.train_no=ROUTES.train_no where STOP1 is null")
        print(self.cur.fetchall())




        
