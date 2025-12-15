import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import pandas as pd

from algorithms.kmeans import KMeans
from utils.data_utils import DataUtils


class CustomerClusteringUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Customer Segmentation - K-Means")
        self.root.geometry("600x480")
        self.root.resizable(False, False)

        self.root.configure(bg="#F5F7FA")
        self.data = None

        self.build_ui()

    # =============================
    # XÂY DỰNG GIAO DIỆN
    # =============================
    def build_ui(self):
        # HEADER
        header = tk.Frame(self.root, bg="#1E88E5", height=90)
        header.pack(fill="x")

        tk.Label(
            header,
            text="PHÂN CỤM KHÁCH HÀNG",
            bg="#1E88E5",
            fg="white",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(18, 0))

        tk.Label(
            header,
            text="Customer Segmentation using K-Means",
            bg="#1E88E5",
            fg="#E3F2FD",
            font=("Segoe UI", 10)
        ).pack()

        # CONTENT
        content = tk.Frame(self.root, bg="#F5F7FA")
        content.pack(padx=30, pady=25, fill="both")

        # LOAD FILE
        tk.Button(
            content,
            text="📂 Chọn file CSV khách hàng",
            command=self.load_file,
            bg="#43A047",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            width=30,
            cursor="hand2"
        ).pack(pady=10)

        self.lbl_file = tk.Label(
            content,
            text="Chưa chọn file",
            bg="#F5F7FA",
            fg="#455A64",
            font=("Segoe UI", 10, "italic")
        )
        self.lbl_file.pack()

        # INPUT K
        frame_k = tk.Frame(content, bg="#F5F7FA")
        frame_k.pack(pady=20)

        tk.Label(
            frame_k,
            text="Số cụm khách hàng (k):",
            bg="#F5F7FA",
            font=("Segoe UI", 11)
        ).pack(side="left")

        self.entry_k = tk.Entry(frame_k, width=10, font=("Segoe UI", 11))
        self.entry_k.pack(side="left", padx=10)
        self.entry_k.insert(0, "3")

        # BUTTON RUN
        tk.Button(
            content,
            text="▶ Phân cụm khách hàng",
            command=self.run_clustering,
            bg="#1E88E5",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            width=25,
            relief="flat",
            cursor="hand2"
        ).pack(pady=15)

        # STATUS
        self.status = tk.Label(
            content,
            text="Sẵn sàng phân tích dữ liệu",
            bg="#F5F7FA",
            fg="#37474F",
            font=("Segoe UI", 10, "italic")
        )
        self.status.pack(pady=10)

    # =============================
    # LOAD FILE CSV
    # =============================
    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")]
        )

        if not file_path:
            return

        try:
            self.data = pd.read_csv(file_path)
            self.lbl_file.config(text=file_path.split("/")[-1])
            self.status.config(text="Đã tải dữ liệu thành công")
        except:
            messagebox.showerror("Lỗi", "Không thể đọc file CSV")

    # =============================
    # CHẠY K-MEANS + VẼ BIỂU ĐỒ ĐẸP
    # =============================
    def run_clustering(self):
        if self.data is None:
            messagebox.showwarning("Thiếu dữ liệu", "Vui lòng chọn file CSV")
            return

        try:
            k = int(self.entry_k.get())
            if k <= 0:
                raise ValueError
        except:
            messagebox.showerror("Lỗi", "Số cụm k không hợp lệ")
            return

        # KIỂM TRA CỘT CẦN THIẾT
        required_cols = ["AnnualIncome", "SpendingScore"]
        for col in required_cols:
            if col not in self.data.columns:
                messagebox.showerror(
                    "Thiếu cột dữ liệu",
                    f"File CSV phải có cột: {col}"
                )
                return

        # LẤY 2 THUỘC TÍNH CÓ Ý NGHĨA
        X_plot = self.data[["AnnualIncome", "SpendingScore"]].values
        X_plot = DataUtils.normalize(X_plot)

        # CHẠY K-MEANS
        model = KMeans(k=k)
        labels = model.fit(X_plot)
        centroids = model.get_centroids()

        self.status.config(
            text=f"Hoàn thành phân cụm khách hàng với k = {k}"
        )

        # ===============================
        # VẼ BIỂU ĐỒ PHÂN CỤM ĐẸP
        # ===============================
        plt.style.use("seaborn-v0_8")
        plt.figure(figsize=(7, 6))

        colors = ["#1E88E5", "#43A047", "#FB8C00", "#8E24AA"]

        for i in range(k):
            plt.scatter(
                X_plot[labels == i, 0],
                X_plot[labels == i, 1],
                s=80,
                color=colors[i % len(colors)],
                label=f"Cụm {i+1}",
                alpha=0.85
            )

        plt.scatter(
            centroids[:, 0],
            centroids[:, 1],
            s=350,
            c="red",
            marker="X",
            label="Tâm cụm"
        )

        plt.title("Phân cụm khách hàng bằng K-Means", fontsize=14, fontweight="bold")
        plt.xlabel("Thu nhập hàng năm (chuẩn hóa)", fontsize=11)
        plt.ylabel("Mức chi tiêu (chuẩn hóa)", fontsize=11)
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()

    def start(self):
        self.root.mainloop()
