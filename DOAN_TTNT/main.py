import pygame
import sys
import random
import ctypes

from map_loader import load_base_map, create_grid
from pathfinder import  a_star

pygame.init()

# CHO PHÉP CÁC EVENT QUAN TRỌNG
pygame.event.set_allowed([
    pygame.KEYDOWN, pygame.KEYUP,
    pygame.MOUSEBUTTONDOWN,
    pygame.QUIT,
    pygame.VIDEORESIZE
])

# ==============================
# TẠO CỬA SỔ
# ==============================
win = pygame.display.set_mode((1100, 800), pygame.RESIZABLE)
pygame.display.set_caption("Hill Climbing vs A* _ Game")

# ==============================
# FIX FOCUS - 100% NHẬN PHÍM
# ==============================
user32 = ctypes.WinDLL("user32")
SW_SHOW = 5

pygame.display.flip()
hwnd = pygame.display.get_wm_info()['window']

user32.ShowWindow(hwnd, SW_SHOW)
user32.SetForegroundWindow(hwnd)
user32.SwitchToThisWindow(hwnd, True)

# ==============================
# FONT
# ==============================
font = pygame.font.SysFont("consolas", 22, bold=True)
small_font = pygame.font.SysFont("consolas", 18)


# ========================================
# RANDOM MAP
# ========================================
def randomize_map(rows, cols, wall_rate=0.30):
    new_map = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("1" if random.random() < wall_rate else "0")
        new_map.append(row)
    return new_map


# ========================================
# VẼ TOÀN BỘ GIAO DIỆN
# ========================================
def draw_window(grid, message="", path_details="", log_text=""):
    W, H = win.get_size()

    win.fill((120, 85, 60))

    map_area_h = int(H * 0.66)
    map_area_w = int(W * 0.70)

    rows = len(grid)
    cols = len(grid[0])

    available_w = max(map_area_w - 20, 50)
    available_h = max(map_area_h - 20, 50)

    cell = min(available_w // cols, available_h // rows)
    map_w = cell * cols
    map_h = cell * rows

    map_x = (map_area_w - map_w) // 2
    map_y = 10

    # Khung bản đồ
    pygame.draw.rect(win, (95, 159, 53), (map_x, map_y, map_w, map_h))
    pygame.draw.rect(win, (167, 116, 73), (map_x + 4, map_y + 4, map_w - 8, map_h - 8))

    # Vẽ các ô
    for r in range(rows):
        for c in range(cols):
            node = grid[r][c]

            if node.width != cell:
                node.resize(cell)

            node.x = map_x + c * cell
            node.y = map_y + r * cell
            node.draw(win)

    # Lưới
    for i in range(rows + 1):
        pygame.draw.line(
            win, (40, 40, 40),
            (map_x, map_y + i * cell),
            (map_x + map_w, map_y + i * cell)
        )

    for j in range(cols + 1):
        pygame.draw.line(
            win, (40, 40, 40),
            (map_x + j * cell, map_y),
            (map_x + j * cell, map_y + map_h)
        )

    # Sidebar
    sidebar_x = map_area_w + 10
    sidebar_y = 10
    sidebar_w = W - map_area_w - 30
    sidebar_h = map_area_h - 20

    pygame.draw.rect(win, (30, 30, 30), (sidebar_x, sidebar_y, sidebar_w, sidebar_h), border_radius=12)
    pygame.draw.rect(
        win, (80, 80, 80),
        (sidebar_x + 4, sidebar_y + 4, sidebar_w - 8, sidebar_h - 8),
        border_radius=12
    )

    cmds = [
        " PHÍM TẮT",
        "",
        "- Chuột trái: chọn A (Start)",
        "- Chuột phải: chọn B (Goal)",
        "- Shift + Chuột trái: đặt vật cản",
        "- V: chạy A*",
        "- X: random map",
        "- C: reset",
        "- ESC: thoát",
    ]

    y = sidebar_y + 20
    for line in cmds:
        txt = small_font.render(line, True, (240, 240, 240))
        win.blit(txt, (sidebar_x + 15, y))
        y += 28

    # Panel dưới
    panel_top = map_area_h + 10
    bottom_h = H - panel_top - 20
    panel_w = (W - 40) // 3

    def draw_panel(x, y, w, h, title, text):
        pygame.draw.rect(win, (20, 20, 20), (x, y, w, h), border_radius=12)
        pygame.draw.rect(
            win, (60, 60, 60),
            (x + 4, y + 4, w - 8, h - 8),
            border_radius=12
        )

        title_surf = small_font.render(title, True, (255, 255, 255))
        win.blit(title_surf, (x + 15, y + 10))

        max_chars = (w - 40) // 9
        lines = [text[i:i + max_chars] for i in range(0, len(text), max_chars)]

        yy = y + 45
        max_lines = (h - 50) // 22

        for line in lines[:max_lines]:
            t = small_font.render(line, True, (220, 220, 220))
            win.blit(t, (x + 15, yy))
            yy += 22

    draw_panel(10, panel_top, panel_w, bottom_h, " Chi tiết đường đi:", path_details)
    draw_panel(20 + panel_w, panel_top, panel_w, bottom_h, " Thông báo:", message)
    draw_panel(30 + panel_w * 2, panel_top, panel_w, bottom_h, " Hành động:", log_text)

    pygame.display.update()


# ========================================
# VỊ TRÍ CLICK
# ========================================
def get_mouse_pos(pos, grid):
    W, H = win.get_size()

    map_area_h = int(H * 0.66)
    map_area_w = int(W * 0.70)

    rows = len(grid)
    cols = len(grid[0])

    available_w = max(map_area_w - 20, 50)
    available_h = max(map_area_h - 20, 50)

    cell = min(available_w // cols, available_h // rows)

    map_w = cell * cols
    map_h = cell * rows

    map_x = (map_area_w - map_w) // 2
    map_y = 10

    x, y = pos
    if not (map_x <= x < map_x + map_w and map_y <= y < map_y + map_h):
        return None, None

    return (y - map_y) // cell, (x - map_x) // cell


# ========================================
# MAIN LOOP
# ========================================
def main():
    base_map = load_base_map("map_5x6.txt")
    grid = create_grid(base_map, 600)

    start = None
    end = None
    msg = "Chọn A (chuột trái), chọn B (chuột phải)."
    path_txt = ""
    log_txt = ""

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        draw_window(grid, msg, path_txt, log_txt)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            # LẤY LẠI FOCUS SAU RESIZE
            if event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                hwnd = pygame.display.get_wm_info()["window"]
                user32.SwitchToThisWindow(hwnd, True)

            # ----------------------------
            # XỬ LÝ CLICK CHUỘT
            # ----------------------------
            if event.type == pygame.MOUSEBUTTONDOWN:

                r, c = get_mouse_pos(event.pos, grid)
                if r is None:
                    continue

                mods = pygame.key.get_mods()

                # SHIFT + LEFT → đặt vật cản
                if event.button == 1 and (mods & pygame.KMOD_SHIFT):
                    node = grid[r][c]
                    if not node.is_start and not node.is_end:
                        node.is_wall = True
                        msg = f"Đã đặt vật cản tại ({r},{c})"
                        log_txt = "Thêm vật cản bằng SHIFT + Left Click."
                    continue

                # Chuột trái → chọn A
                if event.button == 1:
                    if start:
                        start.reset()
                    start = grid[r][c]
                    start.make_start()
                    msg = "Đã chọn A. Chọn B (chuột phải)."
                    log_txt = f"Chọn A tại ({r},{c})"
                    path_txt = ""
                    continue

                # Chuột phải → chọn B
                if event.button == 3:
                    if end:
                        end.reset()
                    end = grid[r][c]
                    end.make_end()
                    msg = "Đã chọn B. Nhấn Z (Hill) hoặc V (A*) để tìm đường."
                    log_txt = f"Chọn B tại ({r},{c})"
                    path_txt = ""
                    continue

            # ----------------------------
            # XỬ LÝ PHÍM
            # ----------------------------
            if event.type == pygame.KEYDOWN:

                # V → chạy A*
                if event.key == pygame.K_v:
                    if start and end:
                        path = a_star(
                            lambda: draw_window(grid, msg, path_txt, log_txt),
                            start, end, grid
                        )
                        if not path:
                            msg = "A* không tìm được đường!"
                            log_txt = "Không có đường hợp lệ."
                            path_txt = ""
                        else:
                            coords = [f"({n.row},{n.col})" for n in path]
                            path_txt = " -> ".join(coords)

                            for n in path:
                                if not n.is_start and not n.is_end:
                                    n.is_path = True
                                    n.animate = True
                                    draw_window(grid, msg, path_txt, log_txt)
                                    pygame.time.delay(30)
                                    n.animate = False

                            msg = "A* tìm đường thành công!"
                            log_txt = f"Số bước (A*): {len(path)-1}"
                    else:
                        msg = "Hãy chọn A và B!"
                        log_txt = "Thiếu điểm!"

                
                if event.key == pygame.K_x:
                    rows = len(grid)
                    cols = len(grid[0])
                    rnd = randomize_map(rows, cols, 0.30)
                    grid = create_grid(rnd, 600)
                    start = end = None
                    msg = "Đã random map mới."
                    log_txt = "Map mới sinh ngẫu nhiên."
                    path_txt = ""

                # C → reset map
                if event.key == pygame.K_c:
                    for row in grid:
                        for node in row:
                            node.reset()
                    start = end = None
                    msg = "Đã reset map!"
                    log_txt = "Reset sạch bản đồ."
                    path_txt = ""

                # ESC → thoát
                if event.key == pygame.K_ESCAPE:
                    run = False

    pygame.quit()
    sys.exit()


# ========================
# RUN GAME
# ========================
if __name__ == "__main__":
    main()
