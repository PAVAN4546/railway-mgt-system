import mysql.connector
class BOOK_TICKETS:
    def __init__(self):
        self.conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pavan@123',
        database='Railway1'
        )

    def trainfetch(self,src,dest):
        self.cur = self.conn.cursor()
        self.cur.execute(f"select routes.train_no,source,stop1,stop2,stop3,stop4,destination from routes inner join train_details on routes.train_no=train_details.train_no where source ='{src}' or stop1='{src}' or stop2='{src}' or stop3='{src}' or stop4='{src}'")
        dt=self.cur.fetchall()
        print(dt)
        try:
            tr=[]
            for i in dt:
                for j in i[i.index(src)+1:]:
                    if j==dest:
                        tr.append(i[0])
        except:
            pass
        return tr
    
    
    def addpassenger(self,pid,pname,age,gen,mno):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO passengers VALUES({pid},'{pname}','{age}',{mno},'{gen}')")
        self.conn.commit()
        print("passengers HAS BEEN INSERTED SUCCESFULLY")
    def addtransaction(self,tid,pid,amount,mode):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES({tid},{pid},{amount},'{mode}')")
        self.conn.commit()
        print("TRANSACTION SUCCESFULL")

        
    def bookticket(self,bid,pid,clas,s_no,tid,scr,dtn,tno):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO BOOK_TICKETS VALUES({bid},'{pid}','{clas}','{s_no}','{tid}','{scr}','{dtn}','{tno}')")
        self.conn.commit()
        print("TICKET HAS BEEN BOOKED")
        print(bid,pid,tid,clas,s_no,scr,dtn,tno)