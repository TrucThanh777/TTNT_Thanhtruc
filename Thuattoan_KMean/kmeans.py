import numpy as np

class KMeans:
    """
    Cài đặt thuật toán K-Means theo hướng đối tượng
    """

    def __init__(self, k, max_iters=100):
        self.k = k
        self.max_iters = max_iters
        self.centroids = None
        self.history = []  # Lưu lịch sử tâm cụm

    def _initialize_centroids(self, X):
        """
        Khởi tạo tâm cụm ngẫu nhiên
        """
        indices = np.random.choice(len(X), self.k, replace=False)
        return X[indices]

    def _assign_clusters(self, X):
        """
        Gán mỗi điểm dữ liệu vào cụm gần nhất
        """
        distances = np.linalg.norm(
            X[:, None] - self.centroids,
            axis=2
        )
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        """
        Cập nhật tâm cụm
        """
        new_centroids = []
        for i in range(self.k):
            cluster_points = X[labels == i]
            if len(cluster_points) == 0:
                new_centroids.append(self.centroids[i])
            else:
                new_centroids.append(cluster_points.mean(axis=0))
        return np.array(new_centroids)

    def fit(self, X):
        """
        Huấn luyện K-Means
        """
        self.centroids = self._initialize_centroids(X)

        for iteration in range(self.max_iters):
            labels = self._assign_clusters(X)
            new_centroids = self._update_centroids(X, labels)

            self.history.append(self.centroids.copy())

            # Kiểm tra hội tụ
            if np.allclose(self.centroids, new_centroids):
                print(f"Hội tụ tại vòng lặp {iteration + 1}")
                break

            self.centroids = new_centroids

        return labels

    def get_centroids(self):
        return self.centroids
