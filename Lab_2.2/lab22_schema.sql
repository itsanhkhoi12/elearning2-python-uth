CREATE DATABASE IF NOT EXISTS library;
USE library;

-- Tạo bảng table
CREATE TABLE books(
	 book_id INT AUTO_INCREMENT PRIMARY KEY,
     book_name VARCHAR(255) NOT NULL,
     author VARCHAR(255) NOT NULL,
     pages INT NOT NULL,
     published_year INT NOT NULL,
     borrowed_status INT NOT NULL, -- 0: có sẵn, 1: đã mượn, 2: trạng thái khác
     category VARCHAR(255) NOT NULL
	);
    
-- Tạo bảng member
CREATE TABLE members(
	member_id INT AUTO_INCREMENT PRIMARY KEY,
    member_name VARCHAR(255) NOT NULL
);

-- Tạo bảng mượn sách
CREATE TABLE borrowing(
	borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
	book_id INT NOT NULL,
    member_id INT NOT NULL,
    borrowing_date DATE NOT NULL,
    due_date DATE,
    returning_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
    );