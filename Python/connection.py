import mysql.connector

class DB_Connector:
    status=False
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='department'
            )
            self.cursor=self.connection.cursor(dictionary=True)
            self.status=True
        except Exception as e:
            self.status=False
            print(e)


    
    
