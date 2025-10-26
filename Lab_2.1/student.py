from datetime import datetime
class Student:
    # Khởi tạo
    def __init__(self,student_id: str,student_name:str,student_dob: datetime, student_email: str, student_phonenumber: str, student_address: str):
        self.student_id = student_id
        self.student_name = student_name
        self.student_dob = student_dob 
        self.student_email = student_email
        self.student_phonenumber = student_phonenumber
        self.student_address = student_address
    # Các thao tác CRUD đối với Table student

    # Thêm một sinh viên
    def add_student(self,db):
        query = "INSERT INTO students (student_id, student_name,student_dob,student_email,student_phonenumber,student_address) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (self.student_id,self.student_name, self.student_dob, self.student_email,self.student_phonenumber,self.student_address)
        db.execute_query(query,params)

    # Cập nhật thông tin của sinh viên
    def update_student(self,db):
        query = "UPDATE students SET student_name = %s, student_dob = %s,  student_email = %s, student_phonenumber = %s, student_address = %s WHERE student_id = %s"
        params =  (self.student_name, self.student_dob, self.student_email, self.student_phonenumber, self.student_address, self.student_id)
        db.execute_query(query,params)

    # Lấy tất cả thông tin về toàn bộ sinh viên
    @staticmethod
    def get_all_student(db):
        query = "SELECT * FROM students"
        result = db.fetch_all(query)
        students_output = []
        for infor in result:
            student_id, student_name,student_dob,student_email,student_phonenumber,student_address = infor
            # Chuyển định dạng ngày sinh DD-MM-YYYY
            formatted_dob = student_dob.strftime("%d-%m-%Y")
            students_output.append((student_id, student_name,formatted_dob,student_email,student_phonenumber,student_address))
        return students_output if students_output else []
    
    # Tìm kiếm một sinh viên
    @staticmethod
    def find_student(db,student_id):
        query = "SELECT * FROM students where student_id = %s"
        param = (student_id,)
        result = db.fetch_all(query,param)
        for infor in result:
            student_id, student_name,student_dob,student_email,student_phonenumber,student_address = infor
            # Ngày sinh được định dạng theo kiểu DD-MM-YYYY
            formatted_dob = student_dob.strftime("%d-%m-%Y")
            student_infor = (student_id, student_name,formatted_dob,student_email,student_phonenumber,student_address)
            return student_infor if student_infor else () 
    
    # Xoá một sinh viên
    @staticmethod
    def delete_student(db,student_id):
        query = "DELETE FROM students WHERE student_id = %s"
        param = (student_id,)
        db.execute_query(query,param)
