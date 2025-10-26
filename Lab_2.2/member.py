class Member:
    def __init__(self, member_name, member_id = None):
        self.member_id = member_id
        self.member_name = member_name
    
    def add_member(self,db):
        query = "INSERT INTO members (member_name) VALUES (%s)"
        db.execute_query(query, (self.member_name,))
    
    @staticmethod
    def delete_member(db,member_id):
        query = "DELETE FROM members WHERE member_id = %s"
        db.execute_query(query,(member_id,))

    def update_member(self,db):
        query = "UPDATE members SET member_name = %s WHERE member_id = %s"
        db.execute_query(query, (self.member_name,self.member_id))
    
    @staticmethod
    def search_member(db, member_id):
        query = "SELECT * FROM members WHERE member_id = %s"
        return db.fetch_one(query, (member_id,))
    
    @staticmethod
    def get_all_members(db):
        query = "SELECT * FROM members"
        return db.fetch_all(query)