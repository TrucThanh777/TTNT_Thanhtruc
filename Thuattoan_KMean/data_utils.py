import numpy as np

class DataUtils:
    """
    Lớp tiện ích xử lý dữ liệu:
    - Sinh dữ liệu mẫu
    - Chuẩn hóa dữ liệu
    """

    @staticmethod
    def generate_data(n_samples=150):
        """
        Sinh dữ liệu 2D ngẫu nhiên
        """
        np.random.seed(42)
        return np.random.rand(n_samples, 2)

    @staticmethod
    def normalize(X):
        """
        Chuẩn hóa Min-Max:
        X_norm = (X - min) / (max - min)
        """
        min_val = X.min(axis=0)
        max_val = X.max(axis=0)
        return (X - min_val) / (max_val - min_val)
