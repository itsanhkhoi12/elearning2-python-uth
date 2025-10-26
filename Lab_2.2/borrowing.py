from datetime import date
from book import Book
class Borrowing:
    def __init__(self, member_id, book_id, borrowing_date = None, due_date = None, returning_date =  None, borrowing_id = None):
        self.borrowing_id = borrowing_id
        self.member_id = member_id
        self.book_id = book_id
        self.borrowing_date = borrowing_date
        self.due_date = due_date
        self.returning_date = returning_date
        
    def borrow_book(self, db):
        def updating_status():
            update_query = "UPDATE books SET borrowed_status = %s WHERE book_id = %s "
            db.execute_query(update_query,(1,self.book_id))

        query = """
        INSERT INTO borrowing (member_id, book_id, borrowing_date, due_date) 
        VALUES (%s, %s, %s, %s)
        """
        params = (self.member_id, self.book_id, self.borrowing_date, self.due_date)
        db.execute_query(query, params)
        updating_status()

    @staticmethod
    # Dùng để tra cứu thông tin thành viên đó mượn sách đã trả chưa?
    def unreturned_book_infor(db,member_id,book_id):
        query = "SELECT * FROM borrowing WHERE member_id = %s AND book_id = %s AND returning_date IS NULL"
        result = db.fetch_one(query,(member_id,book_id))
        return result if result else ()

    @staticmethod
    def return_book(db, returning_date, borrowing_id):

        def updating_status():
            update_query = """
            UPDATE books SET borrowed_status = %s 
            WHERE book_id = (
            SELECT book_id 
            FROM borrowing 
            WHERE borrowing_id = %s
            ) 
            """
            db.execute_query(update_query,(0,borrowing_id))

        query = "UPDATE borrowing SET returning_date = %s WHERE borrowing_id = %s"
        params = (returning_date, borrowing_id)
        db.execute_query(query, params)
        updating_status()
        
    @staticmethod
    def get_overdue_books(db):
        query = """
        SELECT b.book_name, m.member_name, bo.borrowing_date, bo.due_date
        FROM borrowing bo
        JOIN books b ON bo.book_id = b.book_id
        JOIN members m ON bo.member_id = m.member_id
        WHERE bo.returning_date IS NULL AND bo.due_date < %s
        """
        today = date.today()
        return db.fetch_all(query, (today,))
    