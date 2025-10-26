from datetime import datetime, timedelta
from database import Database
from mysql.connector import Error, errorcode
from book import Book
from member import Member
from borrowing import Borrowing

# Hiển thị thông tin chương trình


def display_menu():
    print(f"\n{"CHƯƠNG TRÌNH QUẢN LÝ THƯ VIỆN":=^130}")
    print("(1). Thêm một sách trong thư viện")
    print("(2). Sửa thông tin sách trong thư viện")
    print("(3). Xoá thông tin sách trong thư viện")
    print("(4). Tìm kiếm thông tin sách theo ID")
    print("(5). Tìm kiếm thông tin sách theo tiêu đề")
    print("(6). Hiển thị tất cả sách trong thư viện")
    print("(7). Đăng ký thành viên trong thư viện")
    print("(8). Sửa thông tin một thành viên trong thư viện")
    print("(9). Xoá thông tin một thành viên trong thư viện")
    print("(10). Tìm kiếm thông tin thành viên theo ID")
    print("(11). Hiển thị tất cả thông tin thành viên trong thư viện")
    print("(12). Mượn sách")
    print("(13). Trả sách")
    print("(14). Thông tin sách mượn đã quá hạn")
    print("\tNhập phím bất kỳ để thoát khỏi chương trình")
    print(f"{"="*130}")


if __name__ == "__main__":
    try:
        db = Database()
        print("KẾT NỐI THÀNH CÔNG...")
        while True:
            display_menu()
            code = input("\t(*). Nhập chức năng bất kỳ: ")
            # Thêm, sửa , xoá, cập nhật thông tin sách
            if code == "1":
                title = input("Nhập thông tin tiêu đề sách: ")
                author = input("Nhập họ và tên tác giả: ")
                pages = int(input("Nhập số trang: "))
                published_year = int(input("Nhập năm xuất bản: "))
                status = 0  # Mặc định là khi ta thêm một cuốn sách vào thư viện thì chúng sẽ có sẵn
                category = input("Nhập thể loại: ")
                added_book = Book(title, author, pages,
                                  published_year, status, category)
                added_book.add_book(db)
                print("Đã thêm thông tin của sách thành công!")

            elif code == "2":
                book_id = int(input("Mời bạn nhập ID của sách: "))
                founded_book = Book.search_book(db, book_id)
                if founded_book:
                    title = input("Nhập thông tin tiêu đề sách: ")
                    author = input("Nhập họ và tên tác giả: ")
                    pages = int(input("Nhập số trang: "))
                    published_year = int(input("Nhập năm xuất bản: "))
                    # 0: Có sẵn, 1: Đã mượn, 2: Trạng thái khác
                    status = int(input("Mời bạn nhập trạng thái của sách: "))
                    category = input("Nhập thể loại: ")
                    updated_book = Book(
                        title, author, pages, published_year, status, category, book_id)
                    updated_book.update_book(db)
                    print("Đã cập nhật thông tin của sách thành công")
                else:
                    print("Không tìm thấy sách tương ứng!")

            elif code == "3":
                book_id = int(input("Mời bạn nhập ID của sách: "))
                founded_book = Book.search_book(db, book_id)
                if founded_book:
                    Book.delete_book(db, book_id)
                    print("Đã xoá thông tin về sách đó thành công!")
                else:
                    print("Không tìm thấy sách đó")

            elif code == "4":
                book_title = input("Mời bạn nhập tiêu đề của sách: ").strip()
                founded_book = Book.search_book_by_title(db, book_title)
                if founded_book:
                    print(
                        f"{"ID":<3}{"Tên sách":<40}{"Tác giả":<25}{"Số trang":<10}{"Năm xuất bản":<15}{"Trạng thái":<15}{"Thể loại":<20}")
                    book_id, title, author, pages, published_year, status, category = founded_book
                    print(
                        f"{book_id:<3}{title:<40}{author:<25}{pages:<10}{published_year:<15}{status:<15}{category:<20}")

                else:
                    print("Không tìm thấy sách theo yêu cầu!")

            # Tìm sách theo ID
            elif code == "5":
                book_id = int(input("Mời bạn nhập ID của sách cần tìm kiếm: "))
                founded_book = Book.search_book(db, book_id)
                if founded_book:
                    print(
                        f"{"ID":<3}{"Tên sách":<40}{"Tác giả":<25}{"Số trang":<10}{"Năm xuất bản":<15}{"Trạng thái":<15}{"Thể loại":<20}")
                    book_id, title, author, pages, published_year, status, category = founded_book
                    print(
                        f"{book_id:<3}{title:<40}{author:<25}{pages:<10}{published_year:<15}{status:<15}{category:<20}")

                else:
                    print("Không tìm thấy sách theo yêu cầu!")

            elif code == "6":
                list_of_books = Book.get_all_books(db)
                if list_of_books:
                    print(
                        "\n# Lưu ý: Trạng thái 0 = Có sẵn | 1 = Đã được mượn | 2 = Trạng thái khác")
                    print(f"{"DANH SÁCH CÁC SÁCH TRONG THƯ VIỆN":=^130}")
                    print(
                        f"{"ID":<3}{"Tên sách":<40}{"Tác giả":<25}{"Số trang":<10}{"Năm xuất bản":<15}{"Trạng thái":<15}{"Thể loại":<20}")
                    for book in list_of_books:
                        book_id, title, author, pages, published_year, status, category = book
                        print(
                            f"{book_id:<3}{title:<40}{author:<25}{pages:<10}{published_year:<15}{status:<15}{category:<20}")
                    print(f"{"="*130}")

                else:
                    print("Hiện chưa có sách nào...")

            # CRUD with members
            elif code == "7":
                member_name = input("Nhập họ và tên của bạn: ")
                added_member = Member(member_name)
                added_member.add_member(db)
                print("Đã đăng ký thành viên thành công!")

            elif code == "8":
                member_id = int(input("Mời bạn nhập ID thành viên: "))
                founded_member = Member.search_member(db, member_id)
                if founded_member:
                    member_name = input("Nhập họ và tên của bạn: ")
                    updated_member = Member(member_name, member_id)
                    updated_member.update_member(db)
                    print("Đã cập nhật thông tin thành viên thành công")
                else:
                    print("Không tìm thấy thành viên tương ứng!")

            elif code == "9":
                member_id = int(input("Mời bạn nhập ID thành viên: "))
                founded_member = Member.search_member(db, member_id)
                if founded_member:
                    Member.delete_member(db, member_id)
                    print("Đã xoá thông tin thành viên thành công")
                else:
                    print("Không tìm thấy thành viên tương ứng!")

            elif code == "10":
                member_id = int(
                    input("Mời bạn nhập ID của thành viên cần tìm kiếm: "))
                founded_member = Member.search_member(db, member_id)
                if founded_member:
                    print(f"{"ID":<3}{"Tên thành viên":<40}")
                    member_id, member_name = founded_member
                    print(f"{member_id:<3}{member_name:<40}")
                else:
                    print("Không tìm thấy thành viên theo yêu cầu!")

            elif code == "11":
                list_of_members = Member.get_all_members(db)
                if list_of_members:
                    print(f"{"DANH SÁCH CÁC THÀNH VIÊN TRONG THƯ VIỆN":=^130}")
                    print(f"{"ID":<3}{"Tên thành viên":<40}")
                    for member in list_of_members:
                        member_id, member_name = member
                        print(f"{member_id:<3}{member_name:<40}")
                    print(f"{"="*130}")
                else:
                    print("Hiện chưa có thành viên nào...")

            elif code == "12":
                member_id = input("Nhập ID thành viên: ")
                title = input("Nhập tên sách cần mượn: ")
                book = Book.search_book_by_title(db, title)  # Tìm sách theo tên
                if book:
                    book_id, book_status = book[0], book[5]
                    if book[5] > 0:
                        print("Sách này đã được mượn!")
                    else:
                        borrow_date = datetime.today().strftime('%Y-%m-%d')
                        # Tính ngày trả sách (14 ngày sau ngày mượn)
                        due_date = (datetime.today() +
                                    timedelta(days=14)).strftime('%Y-%m-%d')
                        borrowing = Borrowing(
                            member_id, book_id, borrow_date, due_date)
                        borrowing.borrow_book(db)
                        print(
                            f"Sách '{title}' đã được mượn thành công. Ngày trả sách là {due_date}.")
                else:
                    print(f"Sách '{title}' không tồn tại trong thư viện.")

            elif code == "13":
                member_id = input("Nhập ID thành viên: ")
                title = input("Nhập tên sách bạn đang mượn: ")
                book = Book.search_book_by_title(db, title)  # Tìm sách theo tên
                if book:
                    book_id = book[0]
                    borrowed = Borrowing.unreturned_book_infor(db,member_id,book_id)
                    if borrowed:
                        borrowed_id = borrowed[0]
                        return_date = datetime.today().strftime('%Y-%m-%d')
                        # Cập nhật thông tin trả sách
                        returning = Borrowing(member_id, book_id, None,None, return_date)
                        returning.return_book(db,return_date,borrowed_id)
                        print(f"Sách '{title}' đã được trả thành công. Ngày trả sách là {return_date}.")
                    else:
                        print("Không tồn tại thông tin mượn sách này!")
                else:
                    print(f"Sách '{title}' không tồn tại trong thư viện.")

            elif code == "14":
                overdue_list = Borrowing.get_overdue_books(db)
                if overdue_list:
                    print(f"{"Tên sách":<50}{"Họ và tên thành viên":<25}{"Ngày mượn":<15}{"Ngày mượn":<15}")
                    for overdue in overdue_list:
                        title, member_name, borrowed_date, due_date = overdue
                        borrowed_date = borrowed_date.strftime('%Y-%m-%d')
                        due_date = due_date.strftime('%Y-%m-%d')
                        print(f"{title:<50}{member_name:<25}{borrowed_date:<15}{due_date:<15}")
                else:
                    print("Hiện tại chưa có lượt mượn sách nào quá hạn thời gian để trả lại!")
            else:
                break

    except errorcode.ER_ACCESS_DENIED_ERROR as e:
        print("Bạn đã nhập sai thông tin")
    finally:
        print("KẾT THÚC CHƯƠNG TRÌNH...")
        db.close()
