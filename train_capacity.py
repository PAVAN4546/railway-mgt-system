import mysql.connector
class capacity:
    def __init__(self):
        self.conn=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pavan@123',
        database='Railway1'
        )
    def insertdetails(self,tno,AC_1,AC_2,AC_3,SL,GENERAL):
        self.cur= self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRAIN_CAPACITY VALUES({tno},{AC_1},{AC_2},{AC_3},{SL},{GENERAL})")
        self.conn.commit()
        print("DATA HAS BEEN INSERTED SUCCESFULLY")
    
