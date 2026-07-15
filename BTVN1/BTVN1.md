# BTVN 1 - Python cơ bản

## Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?

Python là một ngôn ngữ lập trình chủ yếu được xem là ngôn ngữ **thông dịch (Interpreted Language)**. Khi chạy chương trình, mã nguồn Python không được biên dịch trực tiếp thành mã máy như C hoặc C++. Thay vào đó, mã nguồn sẽ được biên dịch thành **Bytecode (.pyc)**, sau đó Bytecode được **Python Virtual Machine (PVM)** thông dịch và thực thi.

Vì vậy, Python thường được gọi là ngôn ngữ thông dịch mặc dù bên trong vẫn có bước biên dịch sang Bytecode.

**Ưu điểm:**
- Cú pháp đơn giản, dễ học.
- Chạy trên nhiều hệ điều hành.
- Không cần biên dịch thủ công.

**Nhược điểm:**
- Tốc độ thực thi thường chậm hơn C/C++.

---

## Bài 2

### 1. Các kiểu dữ liệu trong Python

- `int`: Số nguyên
- `float`: Số thực
- `complex`: Số phức
- `str`: Chuỗi ký tự
- `bool`: Kiểu logic (True, False)
- `list`: Danh sách
- `tuple`: Bộ dữ liệu
- `set`: Tập hợp
- `dict`: Từ điển
- `None`: Giá trị rỗng

### 2. Các toán tử trong Python

**Toán tử số học**
- `+` : Cộng
- `-` : Trừ
- `*` : Nhân
- `/` : Chia
- `//` : Chia lấy phần nguyên
- `%` : Chia lấy dư
- `**` : Lũy thừa

**Toán tử so sánh**
- `==`
- `!=`
- `>`
- `<`
- `>=`
- `<=`

**Toán tử gán**
- `=`
- `+=`
- `-=`
- `*=`
- `/=`
- `%=`

**Toán tử logic**
- `and`
- `or`
- `not`

**Toán tử thành viên**
- `in`
- `not in`

**Toán tử định danh**
- `is`
- `is not`

### 3. Mệnh đề điều kiện và vòng lặp

**Mệnh đề điều kiện**
- `if`
- `if...else`
- `if...elif...else`

**Vòng lặp**
- `for`
- `while`

**Lệnh điều khiển vòng lặp**
- `break`
- `continue`
- `pass`

### 4. Kiểu dữ liệu True, False

`True` và `False` thuộc kiểu dữ liệu **bool (Boolean)**. Đây là kiểu dữ liệu dùng để biểu diễn kết quả của các phép so sánh hoặc điều kiện trong chương trình.

Ví dụ:

```python
print(5 > 3)   # True
print(5 < 3)   # False
```

Một số giá trị được coi là **False** trong Python gồm:
- `False`
- `0`
- `0.0`
- `""` (chuỗi rỗng)
- `[]` (danh sách rỗng)
- `{}`
- `()`
- `set()`
- `None`

Các giá trị còn lại thường được coi là **True**.