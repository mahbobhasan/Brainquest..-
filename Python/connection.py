from mysql import connector
class DB_Connector:
    status=False
    def __init__(self):
        try:
            self.connection=connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='department'
            )
            self.cursor=self.connection.cursor(dictionary=True)
            self.status=True
        except Exception as e:
            self.status=False
            print(self.status)
            print(e)
conn=DB_Connector()
print(conn.status)
    
    
