import mysql.connector
import json

# Đọc file .json đã config để kết nối database vào script
with open("./config.json", "r") as f:
    CONFIG =dict(json.loads(f.read()))

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(**CONFIG)
        self.cursor = self.conn.cursor()
    
    def execute_query(self, query, params = None):
        try:
            if params:
                self.cursor.execute(query,params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except mysql.connector.Error as e:
            self.conn.rollback()
            print("Đã gặp lỗi: ", e)
            raise
    
    def fetch_all(self, query, params = None):
        if params:
            self.cursor.execute(query,params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchone()


    def close(self):
        self.cursor.close()
        self.conn.close()
        
        