from mysql import connector
class DB_Connector:
    status=False
    def __init__(self):
        try:
            print('hello')
            self.connection=connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='department'
            )
            print("hello")
            self.cursor=self.connection.cursor(dictionary=True)
            self.status=True
        except Exception as e:
            self.status=False
            print(self.status)
            print(e)

conn=DB_Connector()
    
    
