
# 📘 README – Game Tìm Đường A* (Python – Pygame)

## 🎮 1. Giới thiệu

Đây là game mô phỏng **thuật toán tìm đường** sử dụng hai giải thuật quen thuộc trong Trí tuệ nhân tạo:


- **A\*** (A-Star)

Người chơi có thể chọn điểm **Start** và **Goal**, sau đó quan sát cách hai thuật toán hoạt động, đường đi được tìm, sự khác biệt trong hiệu quả và hạn chế của từng thuật toán.

Game được xây dựng bằng **Python + Pygame**, hỗ trợ:

- Resize cửa sổ (auto scale map)
- Random map mới mỗi lần
- Panel hiển thị chi tiết đường đi, log thao tác, thông báo kết quả
- Texture dạng ảnh (grass, đường, tường,…)

---

## 📁 2. Cấu trúc thư mục dự án

```
📂 Project/
│── main.py               # Giao diện chính + xử lý phím + vòng lặp game
│── map_loader.py         # Load map, texture, tạo grid node
│── node.py               # Định nghĩa Node, resize ô, hiển thị
│── pathfinder.py         # Thuật toán Hill Climbing & A*
│── map_5x6.txt           # File map mẫu (0: đường, 1: tường)
│── run_game.bat          # File chạy nhanh (tùy chọn)
│
└── 📂 images/            # Thư mục chứa ảnh texture (bắt buộc)
      │── grass.png
      │── TUONG.jpg
      │── BD.jpg
      │── KT.jpg
      │── DUONG.png
```

---

## 🛠 3. Cài đặt môi trường

### ✔ Bước 1: Cài Python 3.8 – 3.11

Tải tại: https://www.python.org/downloads/

### ✔ Bước 2: (Khuyến nghị) Tạo môi trường ảo bằng Conda

```bash
conda create -n pathfinding python=3.9
conda activate pathfinding
```

### ✔ Bước 3: Cài thư viện cần thiết

```bash
pip install pygame
```

---

## ▶ 4. Cách chạy game

### **Cách 1 – Chạy trực tiếp từ Terminal**

Mở thư mục project → Shift + Right Click → Open PowerShell:

```bash
python main.py
```

### **Cách 2 – Chạy bằng file run_game.bat**

- Nhấn đúp `run_game.bat`

---

## 🕹 5. Cách chơi & điều khiển

### 🖱 Dùng chuột:
| Hành động | Mô tả |
|----------|--------|
| **Chuột trái** | Chọn điểm **Start (A)** |
| **Chuột phải** | Chọn điểm **Goal (B)** |

---

### ⌨ Phím tắt:
| Phím | Chức năng |
|------|-----------|

| **V** | Chạy thuật toán **A\*** |
| **X** | Tạo **map ngẫu nhiên** mới |
| **C** | Reset lại map hiện tại |
| **ESC** | Thoát game |

---

## 🔄 7. Random Map

Nhấn **X** để tạo map mới:

- Tường sinh ngẫu nhiên theo tỉ lệ `wall_rate = 0.30`
- Các ô được load lại bằng `create_grid()`
- Texture được scale đúng kích thước mới.

---

## ❗ 8. Lỗi thường gặp & cách khắc phục

| Lỗi | Nguyên nhân | Cách sửa |
|-----|--------------|-----------|
| `FileNotFoundError: grass.png` | Thiếu ảnh texture | Thêm đủ 5 file ảnh vào thư mục `images/` |
| Nhấn Z/V không chạy | Chưa chọn Start hoặc Goal | Click chuột trái/chọn A → chuột phải/chọn B |
| Map không hiện | Thiếu file map hoặc sai tên | Đảm bảo file `map_5x6.txt` nằm cùng thư mục |
| Chạy game không hiện cửa sổ | Môi trường chưa cài pygame | `pip install pygame` |

---

## 🏁 9. Yêu cầu hệ thống

- Windows 10/11  
- Python ≥ 3.8  
- Pygame ≥ 2.1  

---

## 📚 10. Tác giả & mục đích học tập

Game được xây dựng nhằm phục vụ môn **Trí Tuệ Nhân Tạo**, giúp sinh viên trực quan hóa hoạt động của thuật toán tìm đường.

