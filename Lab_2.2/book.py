class Book():
    def __init__(self,book_name,author,pages,published_year,status, category, book_id = None):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.published_year = published_year
        self.status = status
        self.category = category

    def add_book(self,db):
        query = "INSERT INTO books (book_name,author, pages, published_year, borrowed_status, category) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (self.book_name,self.author, self.pages, self.published_year, self.status, self.category)
        db.execute_query(query, params)

    def update_book(self, db):
        query = "UPDATE books SET book_name = %s, author = %s, pages = %s, published_year = %s, borrowed_status = %s, category = %s WHERE book_id = %s"
        params = (self.book_name, self.author, self.pages, self.published_year, self.status, self.category, self.book_id)
        db.execute_query(query, params)
    @staticmethod
    def delete_book(db, book_id):
        query = "DELETE FROM books WHERE book_id = %s"
        db.execute_query(query, (book_id,))
    # Tìm sách thông qua mã của chúng
    @staticmethod
    def search_book(db, book_id):
        query = "SELECT * FROM books WHERE book_id = %s"
        return db.fetch_one(query, (book_id,))

    @staticmethod
    def get_all_books(db):
        query = "SELECT * FROM books"
        return db.fetch_all(query)

    # Tìm sách thông qua tiêu đề
    @staticmethod
    def search_book_by_title(db, book_name):
        query = "SELECT * FROM books WHERE book_name = %s"
        return db.fetch_one(query,(book_name,))
