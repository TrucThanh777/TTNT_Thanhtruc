import pygame
from node import Node

# đọc map txt (0 = đường, 1 = tường)
def load_base_map(filename):
    base_map = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().replace(" ", "")  # xóa khoảng trắng nếu có
            if line:
                base_map.append(list(line))
    return base_map
def load_base_map(filename):
    base_map = []
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.strip().replace(" ", "")  # xóa space nếu có
            if line:
                base_map.append(list(line))
    return base_map

# load texture (đảm bảo 5 file này nằm cùng thư mục .py)
grass = pygame.image.load("grass.jpg")
stone = pygame.image.load("TUONG.png")
start_icon = pygame.image.load("BD.PNG")
end_icon = pygame.image.load("KT.jpg")
glow = pygame.image.load("DUONG.png")

# tạo grid node từ map
def create_grid(base_map, map_size):
    rows = len(base_map)
    cols = len(base_map[0])
    w = map_size // cols

    grid = []
    for r in range(rows):
        row_list = []
        for c in range(cols):
            node = Node(r, c, w)
            node.load_textures(grass, stone, start_icon, end_icon, glow)

            if base_map[r][c] == "1":
                node.make_wall()

            row_list.append(node)

        grid.append(row_list)

    return grid
