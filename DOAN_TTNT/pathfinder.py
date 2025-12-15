import math
import heapq


def heuristic(a, b):
    """Heuristic Manhattan: khoảng cách |dx| + |dy| trên grid."""
    return abs(a.row - b.row) + abs(a.col - b.col)


def hill_climbing(draw, start, end, grid):
    """
    Thuật toán Hill Climbing đúng nghĩa:
    - Luôn chọn hàng xóm có heuristic tốt nhất so với mục tiêu.
    - Nếu không có hàng xóm nào tốt hơn current -> kẹt tại local optimum.
    - Có thể KHÔNG tìm được đường đi tới đích.
    """

    rows = len(grid)
    cols = len(grid[0])

    # Reset trạng thái hiển thị / thuật toán
    for row in grid:
        for node in row:
            node.visited = False
            node.flash = False
            if not node.is_start and not node.is_end:
                node.is_path = False
                node.animate = False

    current = start
    path = [start]

    while True:
        # Vẽ từng bước
        draw()

        # Nếu đã tới đích -> trả về đường đi
        if current == end:
            return path

        # Lấy các hàng xóm không phải tường
        neighbors = []
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r = current.row + dr
            c = current.col + dc
            if 0 <= r < rows and 0 <= c < cols:
                nb = grid[r][c]
                if nb.is_wall:
                    continue
                neighbors.append(nb)

        # Không còn hàng xóm hợp lệ -> bế tắc
        if not neighbors:
            current.flash = True  # đánh dấu node bị kẹt
            draw()
            return None

        # Chọn hàng xóm có heuristic nhỏ nhất (tốt nhất)
        best = min(neighbors, key=lambda n: heuristic(n, end))

        # Nếu hàng xóm tốt nhất không cải thiện được heuristic -> local optimum
        if heuristic(best, end) >= heuristic(current, end):
            current.flash = True
            draw()
            return None

        # Đi tới node tốt nhất
        current = best
        path.append(current)


def a_star(draw, start, end, grid):
    """
    Thuật toán A* trên grid:
    - g(n): cost từ start tới n (mỗi bước = 1).
    - h(n): heuristic Manhattan tới đích.
    - f(n) = g(n) + h(n).
    """

    rows = len(grid)
    cols = len(grid[0])

    # Reset trạng thái hiển thị / thuật toán
    for row in grid:
        for node in row:
            node.visited = False
            node.flash = False
            if not node.is_start and not node.is_end:
                node.is_path = False
                node.animate = False

    start_key = (start.row, start.col)
    end_key = (end.row, end.col)

    g_score = {start_key: 0}
    f_score = {start_key: heuristic(start, end)}
    came_from = {start_key: None}

    # heap phần tử: (f, counter, node)
    open_heap = []
    counter = 0
    heapq.heappush(open_heap, (f_score[start_key], counter, start))

    visited = set()

    while open_heap:
        _, _, current = heapq.heappop(open_heap)
        cur_key = (current.row, current.col)

        # Vẽ từng bước
        draw()

        if cur_key in visited:
            continue
        visited.add(cur_key)

        # Nếu tới đích -> dựng lại đường đi
        if current == end:
            path = []
            key = cur_key
            while key is not None:
                r, c = key
                path.append(grid[r][c])
                key = came_from[key]
            path.reverse()
            return path

        # Duyệt 4 hướng
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rr = current.row + dr
            cc = current.col + dc
            if 0 <= rr < rows and 0 <= cc < cols:
                nb = grid[rr][cc]
                if nb.is_wall:
                    continue

                nb_key = (nb.row, nb.col)
                tentative_g = g_score[cur_key] + 1

                if nb_key not in g_score or tentative_g < g_score[nb_key]:
                    g_score[nb_key] = tentative_g
                    f = tentative_g + heuristic(nb, end)
                    f_score[nb_key] = f
                    came_from[nb_key] = cur_key

                    counter += 1
                    heapq.heappush(open_heap, (f, counter, nb))

    # Không tìm được đường
    return None
