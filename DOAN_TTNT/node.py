import pygame

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.width = width
        self.x = col * width
        self.y = row * width

        # trạng thái logic
        self.is_wall = False
        self.is_start = False
        self.is_end = False
        self.is_path = False
        self.visited = False

        # trạng thái hiệu ứng
        self.animate = False
        self.flash = False

        # texture đang dùng (đã scale)
        self.tex_normal = None
        self.tex_wall = None
        self.tex_start = None
        self.tex_end = None
        self.tex_glow = None

        # texture gốc (chưa scale)
        self.orig_normal = None
        self.orig_wall = None
        self.orig_start = None
        self.orig_end = None
        self.orig_glow = None

    def reset_for_search(self):
        """Reset khi chạy lại thuật toán tìm đường"""
        if not self.is_start and not self.is_end:
            self.is_path = False
            self.animate = False
            self.visited = False
            self.flash = False

    def resize(self, w):
        """Scale lại texture theo kích thước mới của ô – dùng bản gốc để tránh méo"""
        self.width = w
        self.x = self.col * w
        self.y = self.row * w

        def scale(tex):
            return pygame.transform.scale(tex, (w, w)) if tex else None

        # scale từ bản gốc, KHÔNG scale chồng lên texture cũ
        self.tex_normal = scale(self.orig_normal)
        self.tex_wall = scale(self.orig_wall)
        self.tex_start = scale(self.orig_start)
        self.tex_end = scale(self.orig_end)
        self.tex_glow = scale(self.orig_glow)

    def load_textures(self, normal, wall, start, end, glow):
        """Lưu bản gốc và scale lần đầu"""
        self.orig_normal = normal
        self.orig_wall = wall
        self.orig_start = start
        self.orig_end = end
        self.orig_glow = glow

        # scale lần đầu
        self.resize(self.width)

    def make_wall(self):
        self.is_wall = True
        self.is_start = False
        self.is_end = False
        self.is_path = False

    def make_start(self):
        self.is_start = True
        self.is_end = False
        self.is_wall = False
        self.is_path = False

    def make_end(self):
        self.is_end = True
        self.is_start = False
        self.is_wall = False
        self.is_path = False

    def reset(self):
        """Reset hoàn toàn node (dùng cho phím C)"""
        self.is_wall = False
        self.is_start = False
        self.is_end = False
        self.is_path = False
        self.visited = False
        self.animate = False
        self.flash = False

    def draw(self, win):
        # Tường
        if self.is_wall:
            win.blit(self.tex_wall, (self.x, self.y))
            return

        # Flash đỏ (nếu muốn đánh dấu lỗi / kẹt)
        if self.flash:
            win.blit(self.tex_wall, (self.x, self.y))
            overlay = pygame.Surface((self.width, self.width), pygame.SRCALPHA)
            overlay.fill((255, 0, 0, 150))
            win.blit(overlay, (self.x, self.y))
            return

        # Ô đang animate (đi qua)
        if self.animate and not self.is_start and not self.is_end:
            win.blit(self.tex_glow, (self.x, self.y))
            return

        # Start
        if self.is_start:
            win.blit(self.tex_normal, (self.x, self.y))
            win.blit(self.tex_start, (self.x, self.y))
            return

        # End
        if self.is_end:
            win.blit(self.tex_normal, (self.x, self.y))
            win.blit(self.tex_end, (self.x, self.y))
            return

        # Đường đi đã tìm được
        if self.is_path and not self.is_start and not self.is_end:
            win.blit(self.tex_glow, (self.x, self.y))
            return

        # Ô thường
        win.blit(self.tex_normal, (self.x, self.y))
