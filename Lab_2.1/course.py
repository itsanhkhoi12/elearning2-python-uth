class Course:
    # Khởi tạo
    def __init__(self,course_id: str,course_name:str,course_credits:int, course_description = None):
        self.course_id = course_id
        self.course_name = course_name
        self.course_credits = course_credits
        self.course_description = course_description

    # Các thao tác CRUD đối với Table Course

    # Thêm một một học
    def add_course(self,db):
        query = "INSERT INTO courses (course_id, course_name,course_credits,course_description) VALUES (%s,%s,%s,%s)"
        params = (self.course_id,self.course_name,self.course_credits,self.course_description)
        db.execute_query(query,params)

    # Cập nhật thông tin của môn học
    def update_course(self,db):
        query = "UPDATE courses SET course_name = %s, course_credits = %s, course_description = %s WHERE course_id = %s"
        params = (self.course_name, self.course_credits,self.course_description,self.course_id)
        db.execute_query(query,params)

    # Lấy tất cả thông tin về khoá học hiện có
    @staticmethod
    def get_all_course(db):
        query = "SELECT * FROM courses"
        result = db.fetch_all(query)
        courses_output = []
        for infor in result:
            course_id,course_name,course_description,course_credits = infor
            courses_output.append((course_id,course_name,course_description,course_credits))
        # Trả về danh sách các môn học nếu có, không thì trả về danh sách rỗng
        return courses_output if courses_output else []
    
    # Tìm kiếm một khoá học
    @staticmethod
    def find_course(db,course_id):
        query = "SELECT * FROM courses where course_id = %s"
        param = (course_id,)
        result = db.fetch_all(query,param)
        for infor in result:
            course_id,course_name,course_description,course_credits = infor
            course_infor = (course_id,course_name,course_description,course_credits)
            return course_infor if course_infor else ()
    
    # Xoá một khoá học
    @staticmethod
    def delete_course(db,course_id):
        query = "DELETE FROM courses WHERE course_id = %s"
        param = (course_id,)
        db.execute_query(query,param)
