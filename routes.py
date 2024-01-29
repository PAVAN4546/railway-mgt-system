import mysql.connector
class ROUTES:
    def __init__(self):
        self.conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pavan@123',
        database='Railway1'
        )
    def insertdetails(self,tno,stop1,stop2,stop3,stop4):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO ROUTES VALUES({tno},'{stop1}','{stop2}','{stop3}','{stop4}')")
        self.conn.commit()
        print("DATA HAS BEEN INSERTED SUCCESFULLY")
    def fetchdetails(self,source,destination):
        self.cur=self.con.cursor()
        self.cur.execute(f"select train_details.train_no,train_name,source,stop1,stop2,stop3,stop4,destination from train_details inner join routes on train_details.train_no=routes.train_no where source='{source}' or stop1='{source}' or stop2='{source}' or stop3='{source}' or stop4='{source}'")
        train_details=self.cur.fetchall()
        train_no=[]
        for i in train_details:
            stop=i.index(source)
            routes=i[stop+1:]
            if destination in routes:
                train_no.append(i[0])
        print(train_no)