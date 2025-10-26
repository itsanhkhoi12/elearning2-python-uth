from datetime import datetime
class Enrollment:
    # Khởi tạo
    def __init__(self, student_id: str,course_id: str, enrolled_date = datetime.now().date()):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.enrolled_date = enrolled_date

    # Các thao tác CRUD đối với Table enrollment

    # Đăng ký môn học
    def enrollment_course(self,db):
        query = "INSERT INTO enrollment (student_id,course_id) VALUES (%s,%s)"
        params = (self.student_id,self.course_id)
        db.execute_query(query,params)
    
    # Tìm kiếm tất cả khoá học mà sinh viên đó đã đăng ký
    @staticmethod
    def find_student_enrollment(db,student_id):
        query = "SELECT course_id, enrolled_date FROM enrollment WHERE student_id = %s"
        param = (student_id,)
        result = db.fetch_all(query,param)
        student_infor = []
        for infor in result:
            course_id, enrolled_date = infor
            formatted_date = enrolled_date.strftime("%d-%m-%Y")
            student_infor.append((course_id,formatted_date))
    
        return student_infor if student_infor else []
    
    # Xoá một lượt đăng ký khoá học của sinh viên đó
    @staticmethod
    def delete_enrolled_course(db,student_id, course_id):
        query = "DELETE FROM enrollment WHERE student_id = %s AND course_id = %s"
        param = (student_id, course_id)
        db.execute_query(query,param)
