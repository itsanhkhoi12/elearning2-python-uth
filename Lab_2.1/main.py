import textwrap
from database import Database
from student import Student
from course import Course
from enrollment import Enrollment
from mysql.connector import errorcode

try:
    db = Database()
    print("ĐÃ KẾT NỐI THÀNH CÔNG...\n")
    while True:
        print(f"\n{"MENU ĐĂNG KÝ HỌC PHẦN":=^130}")
        print("(1). Thêm một sinh viên")
        print("(2). Xoá thông tin một sinh viên")
        print("(3). Cập nhật thông tin của sinh viên")
        print("(4). Tìm kiến một sinh viên")
        print("(5). Hiển thị tất cả sinh viên")
        print("(6). Thêm một khoá học")
        print("(7). Cập nhật thông tin của khoá học")
        print("(8). Tìm kiếm một khoá học")
        print("(9). Hiển thị tất cả thông tin của các khoá học")
        print("(10). Xoá khoá học đó")
        print("(11). Đăng ký một môn học")
        print("(12). Hiển thị tất cả các môn học mà sinh viên đó đã đăng ký")
        print("(13). Xoá lượt đăng ký môn học của sinh viên")
        print(f"{"="*130}")
        print("\n\tNhấn bất kỳ các phím còn lại để kết thúc chương trình...")
        print("\t(*). Nhập * để thực hiện các chức năng. ")
        choice = input("\nMời bạn nhập một chức năng của chương trình: ")
            # Chức năng của sinh viên (1-5)
        if (choice == "1"):
            id = input("Mời bạn nhập MSSV của sinh viên: ").strip()
            name = input("Mời bạn nhập Họ và tên của sinh viên: ").strip()
            dob = input("Mời bạn nhập ngày sinh của sinh viên (Nhập theo định dạng YYYY-MM-DD): ").strip()
            email = input("Mời bạn nhập email của sinh viên: ").strip()
            phonenumber = input("Mời bạn nhập số điện thoại của sinh viên: ").strip()
            address = input("Mời bạn nhập địa chỉ của sinh viên: ").strip()
            infor = Student(id,name,dob,email,phonenumber,address)
            infor.add_student(db)
            print("Đã thêm thành công một sinh viên!")
        
        elif (choice == "2"):
            id = input("Mời bạn nhập MSSV của sinh viên: ")
            student = Student.find_student(db,id)
            if student:
                Student.delete_student(db,id)
                print("Đã xoá thành công thông tin của sinh viên")
            else:
                print("Không tìm thấy sinh viên này")
        
        elif (choice == "3"):
            id = input("Mời bạn nhập MSSV của sinh viên: ")
            student = Student.find_student(db,id)
            if student:
                name = input("Mời bạn nhập Họ và tên mới của sinh viên: ").strip()
                dob = input("Mời bạn nhập ngày sinh mới của sinh viên (Nhập theo định dạng YYYY-MM-DD): ").strip()
                email = input("Mời bạn nhập email mới của sinh viên: ").strip()
                phonenumber = input("Mời bạn nhập số điện thoại mới của sinh viên: ").strip()
                address = input("Mời bạn nhập địa chỉ mới của sinh viên: ").strip()
                updated_student = Student(id,name,dob,email,phonenumber,address)
                updated_student.update_student(db)
                print("Đã cập nhật thông tin thành công!")
            else:
                print("Không tìm thấy sinh viên này")
        
        elif choice == "4":
            id = input("Mời bạn nhập MSSV: ")
            student = Student.find_student(db,id)
            if student:
                print(f"{'MSSV':<10}{'Họ và tên':<25}{"Ngày sinh":<15}{'Email':<30}{'SĐT':<15}{'Địa chỉ':<30}")                
                name, dob, email, phonenumber, address = student[1:]
                print(f"{id:<10}{name:<25}{dob:<15}{email:<30}{phonenumber:<15}{address:<30}")
            else:
                print("Không tìm thấy sinh viên này")
        
        elif choice == "5":
            students = Student.get_all_student(db)
            if students:
                count = 1
                print("\n")
                print(f"{'DANH SÁCH SINH VIÊN':=^110}")
                print(f"{"STT":<5}{'MSSV':<10}{'Họ và tên':<25}{"Ngày sinh":<15}{'Email':<30}{'SĐT':<15}{'Địa chỉ':<30}")                
                for student in students:
                    id, name, dob, email, phonenumber, address = student
                    print(f"{count:<5}{id:<10}{name:<25}{dob:<15}{email:<30}{phonenumber:<15}{address:<30}")
                    count+=1
                print(f"{"="*110}")
            else:
                print("Hiện tại chưa có sinh viên nào...")

            # Chức năng thao tác với khoá học (6-10)
        elif choice == "6":
            id = input("Mời bạn nhập mã môn học: ").strip()
            course_name = input("Mời bạn nhập tên khoá học: ").strip()
            course_credit = int(input("Mời bạn nhập số tín chỉ của môn học: "))
            course_description = input("Mời bạn nhập mô tả về khoá học này: ").strip()
            infor = Course(id,course_name,course_credit, course_description)
            infor.add_course(db)
            print("Đã thêm thành công một môn học!")
        
        elif choice == "7":
            id = input("Mời bạn nhập mã môn học: ")
            course = Course.find_course(db,id)
            if id:
                course_name = input("Mời bạn nhập tên mới của khoá học: ").strip()
                course_credit = int(input("Mời bạn cập nhật số tín chỉ của môn học: "))
                course_description = input("Mời bạn cập nhật mô tả về khoá học này: ").strip()
                updated_course = Course(id,course_name,course_credit,course_description)
                updated_course.update_course(db)
                print("Đã cập nhật thông tin thành công!")
            else:
                print("Không tìm thấy môn học này...")
        
        elif choice == "8":
            id = input("Mời bạn nhập mã môn học: ")
            course = Course.find_course(db,id)
            if course:
                course_name, course_description, course_credits = course[1:]
                # In các thông tin của môn học đó
                print("Mã môn học: ",id)
                print("Tên môn học: ",course_name)
                print("Mô tả về môn học: ",textwrap.fill(course_description,width=80))
                print("Số tín chỉ: ",course_credits)
            else:
                print("Không tìm thấy môn học này...")
        
        elif choice == "9":
            courses = Course.get_all_course(db)
            if courses:
                count = 1
                print(f"{'DANH SÁCH CÁC KHOÁ HỌC':=^110}")
                for course in courses:
                    print(f"\nMôn học thứ {count}")
                    id, course_name, course_description, course_credits = course
                    # In các thông tin của môn học đó
                    print("Mã môn học: ",id)
                    print("Tên môn học: ",course_name)
                    print("Mô tả về môn học: ",textwrap.fill(course_description,width=80))
                    print("Số tín chỉ: ",course_credits)
                    count+=1
                print(f"{"="*110}")
            else:
                print("Hiện tại chưa có sinh viên nào...")

        elif choice == "10":
            id = input("Mời bạn nhập mã môn học: ").strip()
            course = Course.find_course(db,id)
            if course:
                Course.delete_course(db,id)
                print("Đã xoá môn học thành công!")
            else:
                print("Không tìm thấy môn học này")

            # Chức năng đăng ký khoá học (11-13)
        elif choice == "11":
            student_id = input("Mời bạn nhập MSSV: ").strip()
            course_id = input("Mời bạn nhập mã môn học: ").strip()
            if Course.find_course(db, course_id) and Student.find_student(db,student_id):
                enrollment = Enrollment(student_id,course_id)
                enrollment.enrollment_course(db)
                print("Đã đăng ký môn học có mã {} thành công".format(course_id))
            else:
                print("Thông tin đăng ký khoá học không hợp lệ!")
        
        elif choice == "12":
            student_id = input("Mời bạn nhập MSSV: ").strip()
            if student_id:
               enrollment_list = Enrollment.find_student_enrollment(db,student_id)
               count = 1
               print(f"{'DANH SÁCH MÔN HỌC ĐÃ ĐĂNG KÝ':=^50}")
               print(f"{'STT':<5}{'Mã môn học':<15}{'Ngày đăng ký':<15}")
               for course in enrollment_list:
                   course_id, enrolled_date = course
                   print(f"{count:<5}{course_id:<15}{enrolled_date:<15}")
                   count+=1
               print(f"{"="*50}")                   
            else:
                print("Không tìm thấy sinh viên này!")
        
        elif choice == "13":
            student_id = input("Mời bạn nhập MSSV: ").strip()
            course_id = input("Mời bạn nhập môn học cần xoá: ").strip()
            if(student_id and course_id):
                Enrollment.delete_enrolled_course(db,student_id,course_id)
                print("Đã xoá lượt đăng ký môn học {} thành công!".format(course_id))
            else:
                print("Không tìm thấy MSSV hoặc môn học!")

        else:
            break
except errorcode.ER_DB_ACCESS_DENIED as e:
    print("KẾT NỐI THẤT BẠI...")
finally:
    print("DỌN CHƯƠNG TRÌNH...")
    db.close()
