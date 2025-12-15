README – Phân Cụm Khách Hàng bằng K-Means (Python)
1. Giới thiệu

Đây là chương trình mô phỏng thuật toán phân cụm K-Means, một thuật toán học không giám sát (Unsupervised Learning) trong Trí tuệ nhân tạo.

Chương trình cho phép:

Nạp dữ liệu khách hàng từ file CSV

Chọn số cụm K

Thực hiện phân cụm bằng thuật toán K-Means

Quan sát kết quả phân nhóm và trực quan hóa dữ liệu

Ứng dụng được xây dựng bằng Python, có giao diện đơn giản (Tkinter) và biểu đồ hiển thị kết quả bằng Matplotlib.

 2. Cấu trúc thư mục dự án
 KMEANS_PROJECT/
│── main.py                 # File chạy chính, giao diện người dùng
│
├── algorithms/
│   └── kmeans.py           # Cài đặt thuật toán K-Means
│
├── utils/
│   └── data_utils.py       # Đọc và xử lý dữ liệu CSV
│
├── data/
│   └── customers.csv       # Dữ liệu khách hàng mẫu
│
└── README.md               # File hướng dẫn
 3. Thuật toán K-Means
 Ý tưởng

Thuật toán K-Means chia tập dữ liệu thành K cụm, sao cho:

Các điểm trong cùng cụm gần nhau nhất

Khoảng cách từ điểm dữ liệu đến tâm cụm là nhỏ nhất

✔ Các bước thực hiện

Chọn số cụm K

Khởi tạo ngẫu nhiên K tâm cụm

Gán mỗi điểm dữ liệu vào cụm có tâm gần nhất

Cập nhật lại tâm cụm bằng trung bình các điểm trong cụm

Lặp lại bước 3–4 cho đến khi hội tụ

 Công thức khoảng cách Euclidean
d(x, y) = sqrt( Σ (xi − yi)² )
🛠 4. Cài đặt môi trường
 Bước 1: Cài Python 3.8 – 3.11

Tải tại: https://www.python.org/downloads/
 Bước 2: (Khuyến nghị) Tạo môi trường ảo bằng Conda
conda create -n kmeans_env python=3.9
conda activate kmeans_env
 Bước 3: Cài các thư viện cần thiết
pip install numpy pandas matplotlib

tkinter đã có sẵn trong Python

 5. Chuẩn bị dữ liệu

File dữ liệu phải có định dạng CSV, ví dụ:

Age,Income,SpendingScore
23,15,39
45,30,81
31,28,6

Mỗi dòng là một khách hàng

Các cột là thuộc tính dùng để phân cụm

 6. Cách chạy chương trình

Mở Terminal tại thư mục project:

python main.py

Sau khi chạy:

Chọn file CSV

Nhập số cụm K

Nhấn Run K-Means để thực hiện phân cụm

 7. Chức năng chính
Chức năng	Mô tả
Load CSV	Nạp dữ liệu khách hàng
Chọn K	Nhập số cụm cần phân
Run K-Means	Thực hiện thuật toán
Visualize	Hiển thị biểu đồ phân cụm
 8. Kết quả

Dữ liệu được chia thành K nhóm khách hàng

Mỗi nhóm được tô màu khác nhau trên biểu đồ

Tâm cụm được hiển thị rõ ràng

 9. Lỗi thường gặp & cách khắc phục
Lỗi	Nguyên nhân	Cách sửa
Không load được CSV	Sai định dạng file	Kiểm tra file .csv
Chương trình không chạy	Thiếu thư viện	pip install numpy pandas matplotlib
Biểu đồ không hiện	Dữ liệu không hợp lệ	Kiểm tra số cột dữ liệu
K quá lớn	K > số dòng dữ liệu	Giảm K
 10. Yêu cầu hệ thống

Windows 10/11

Python ≥ 3.8

NumPy, Pandas, Matplotlib

---- 11. Ứng dụng thực tế----

Phân nhóm khách hàng

Phân tích hành vi người dùng

Marketing & gợi ý sản phẩm

Khai phá dữ liệu (Data Mining)

----12. Tác giả & mục đích học tập-----

Sinh viên: Phạm Thanh Trúc

Môn học: Trí Tuệ Nhân Tạo

Thuật toán: K-Means Clustering