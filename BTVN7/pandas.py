
import pandas as pd

data = {
    "student_id": [
        "SV009", "SV002", "SV006", "SV001", "SV005",
        "SV003", "SV010", "SV004", "SV007", "SV008"
    ],

    "name": [
        "Minh", "Hoang", "Binh", "Dung", "Lan",
        "Son", "Do", "Dat", "Chi", "An"
    ],

    "class": [
        "CNTT01", "CNTT02", "CNTT01", "CNTT01", "CNTT02",
        "CNTT03", "CNTT03", "CNTT01", "CNTT03", "CNTT02"
    ],

    "city": [
        "Hai Duong", "Nghe An", "Nam Dinh", "Phu Tho", "Ha Noi",
        "Ha Noi", "Cao Bang", "Nam Dinh", "Ha Noi", "Ha Noi"
    ],

    "giai_tich": [
        5.5, 7.0, 9.5, 8.5, 8.0,
        9.0, 7.0, 6.5, 7.5, 8.0
    ],

    "triet": [
        6.0, 6.5, 9.5, 8.0, 8.0,
        9.0, 7.0, 7.0, 7.5, 8.5
    ],

    "dstt": [
        6.0, 8.0, 9.0, 9.0, 8.0,
        9.5, 7.0, 7.0, 7.5, 8.5
    ]
}

df = pd.DataFrame(data)

df

"""### Dữ liệu gồm:

- 10 sinh viên, 7 cột.
- Các lớp có trong dữ liệu: `CNTT01`, `CNTT02`, `CNTT03`
- Các thành phố: `Hai Duong`, `Nghe An`, `Nam Dinh`, `Phu Tho`, `Ha Noi`, `Cao Bang`
- Cột điểm: `giai_tich`, `triet`, `dstt`

## 1. Khám phá dữ liệu

### Bài 1

Với DataFrame `df`, hãy:

1. Hiển thị **5 dòng đầu**.
2. Hiển thị **5 dòng cuối**.
3. Cho biết DataFrame có bao nhiêu **dòng** và bao nhiêu **cột**.
4. Hiển thị **danh sách tên các cột**.
5. Xem **thông tin tổng quan** (số dòng, tên cột, kiểu dữ liệu từng cột).

<details>
<summary>Gợi ý</summary>

Bạn cần 5 thứ: `.head()`, `.tail()`, `.shape`, `.columns`, `.info()`
</details>

**Tự kiểm tra:** `shape` phải ra `(10, 7)`. `info()` phải cho thấy 4 cột kiểu `object` (chữ) và 3 cột kiểu `float64` (số).
"""

df.head()

df.tail()

print(df.shape)

print(df.columns)

df.info()

"""
## 2. Chọn dữ liệu

### Bài 2

Từ `df`, hãy lấy:

1. Cột `name`
2. Cột `class`
3. Hai cột `name` và `city`
4. Bốn cột `name`, `giai_tich`, `triet`, `dstt`

<details>
<summary>Gợi ý</summary>

- Một cột → `df["name"]` → kết quả là một **Series** (một dãy giá trị)
- Nhiều cột → `df[["name", "city"]]` → kết quả là một **DataFrame** (một bảng)

Nhiều cột cần **hai lớp ngoặc vuông** `[[ ]]`, vì bên trong là một **list** tên cột.
</details>

**Tự kiểm tra:** chạy `type(df["name"])` và `type(df[["name"]])` — hai kết quả phải **khác nhau** (`Series` vs `DataFrame`)."""

df["name"]
df["class"]
df[["name", "city"]]
df[["name", "giai_tich", "triet", "dstt"]]

"""
## 3. Lọc dữ liệu

### Bài 3 — Lọc 1 điều kiện

Hãy tìm:

1. Sinh viên có `giai_tich >= 8`
2. Sinh viên có `triet >= 8`
3. Sinh viên thuộc lớp `CNTT01`
4. Sinh viên đến từ `Ha Noi`

<details>
<summary>Gợi ý</summary>

Công thức chung: `df[ điều_kiện ]`

```python
df[df["giai_tich"] >= 8]
```

Với chuỗi thì dùng `==`:

```python
df[df["class"] == "CNTT01"]
```

Chưa hiểu tại sao cú pháp lại như vậy? Thử chạy riêng dòng này xem nó trả về gì:

```python
df["giai_tich"] >= 8
```
</details>

**Tự kiểm tra:** kết quả lần lượt phải có **5, 5, 4, 4** dòng."""

df[df["giai_tich"] >= 8]
df[df["triet"] >= 8]
df[df["class"] == "CNTT01"]
df[df["city"] == "Ha Noi"]

"""### Bài 4 — Lọc nhiều điều kiện (Và)

1. Tìm sinh viên thỏa mãn **đồng thời**: `giai_tich >= 8` **và** `dstt >= 8`
2. Tìm sinh viên **thuộc lớp `CNTT01`** **và** có `giai_tich >= 8`

<details>
<summary>Gợi ý</summary>

Trong Pandas, "và" là `&` — không dùng `and`.

Mỗi điều kiện phải bọc trong một cặp ngoặc tròn riêng:

```python
df[(điều_kiện_1) & (điều_kiện_2)]
```
</details>

**Tự kiểm tra:** câu 1 ra **5 dòng**, câu 2 ra **2 dòng** (Binh và Dung).
"""

df[(df["giai_tich"] >= 8) & (df["dstt"] >= 8)]
df[(df["class"] == "CNTT01") & (df["giai_tich"] >= 8)]

"""### Bài 5 — Lọc nhiều điều kiện (Hoặc)

Tìm sinh viên thỏa mãn **ít nhất một trong hai**:

- `giai_tich >= 9`
- `dstt >= 9`

<details>
<summary>Gợi ý</summary>

"Hoặc" là `|` — **không** dùng `or`.
</details>

**Tự kiểm tra:** ra **3 dòng** (Binh, Dung, Son).
"""

df[(df["giai_tich"] >= 9) | (df["dstt"] >= 9)]

"""## 4. Sắp xếp dữ liệu

### Bài 6

1. Sắp xếp toàn bộ sinh viên theo `giai_tich` **tăng dần**.
2. Sắp xếp toàn bộ sinh viên theo `giai_tich` **giảm dần**.
3. Sắp xếp theo `dstt` **giảm dần**, rồi chỉ hiển thị **3 sinh viên đầu tiên**.

<details>
<summary>Gợi ý</summary>

```python
df.sort_values("tên_cột")                     # mặc định: tăng dần
df.sort_values("tên_cột", ascending=False)    # giảm dần
```
</details>

**Tự kiểm tra:**
- Câu 1: dòng đầu là **Minh** (5.5). Câu 2: dòng đầu là **Binh** (9.5).
- Câu 3: đúng **3 dòng** — Son (9.5), rồi Binh và Dung (đều 9.0).
"""

df.sort_values("giai_tich")
df.sort_values("giai_tich", ascending=False)
df.sort_values("dstt", ascending=False).head(3)

"""## 5. Bài luyện tổng hợp

### Bài 7

Tìm các sinh viên có `giai_tich >= 8` **và** `dstt >= 8`. Sau đó:

1. Sắp xếp theo `giai_tich` **giảm dần**
2. Chỉ hiển thị các cột: `name`, `class`, `giai_tich`, `dstt`

<details>
<summary>Gợi ý</summary>

Chia thành 3 bước, làm xong bước nào chạy thử bước đó:

```
Bước 1 — lọc:      kq = df[(...) & (...)]
Bước 2 — sắp xếp:  kq = kq.sort_values(...)
Bước 3 — chọn cột: kq = kq[["name", "class", ...]]
```

Ra đúng rồi, hãy thử viết lại thành **một dòng duy nhất** bằng cách nối liên tiếp dấu `.`
</details>

**Tự kiểm tra:** bảng ra **5 dòng × 4 cột**, thứ tự tên: **Binh → Son → Dung → Lan → An**.
"""

df[(df["giai_tich"] >= 8) & (df["dstt"] >= 8)] \
    .sort_values("giai_tich", ascending=False) \
    [["name", "class", "giai_tich", "dstt"]]

"""---
#MINI TEST

## Bài 8

Tìm **5 sinh viên có điểm `triet` cao nhất**.

Kết quả chỉ hiển thị: `name`, `class`, `triet`

**Tự kiểm tra:** 5 dòng × 3 cột. Người đứng đầu có `triet` = 9.5.
"""

df.sort_values("triet", ascending=False) \
    .head(5)[["name", "class", "triet"]]

"""## Bài 9

Tìm những sinh viên thỏa mãn **cả ba** điều kiện:

- `giai_tich >= 8`
- `triet >= 7`
- `dstt >= 8`

Sau đó sắp xếp theo `dstt` **giảm dần**.

Chỉ hiển thị: `name`, `class`, `giai_tich`, `triet`, `dstt`

**Tự kiểm tra:** 5 dòng × 5 cột, dòng đầu là **Son**.
"""

df[
    (df["giai_tich"] >= 8) &
    (df["triet"] >= 7) &
    (df["dstt"] >= 8)
].sort_values("dstt", ascending=False)[
    ["name", "class", "giai_tich", "triet", "dstt"]
]

"""## Bài 10

Tìm sinh viên có điểm `giai_tich` **cao nhất trong lớp `CNTT01`**.

Kết quả hiển thị: `name`, `class`, `giai_tich`

Chỉ dùng những gì đã học ở trên. Gợi ý duy nhất: *"cao nhất" = "sắp xếp giảm dần rồi lấy dòng đầu tiên"*.

**Tự kiểm tra:** kết quả là **1 dòng** duy nhất.
"""

df[df["class"] == "CNTT01"] \
    .sort_values("giai_tich", ascending=False) \
    .head(1)[["name", "class", "giai_tich"]]