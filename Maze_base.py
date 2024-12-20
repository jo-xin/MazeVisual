import random

# 第一种表达方式，墙壁和通道都占位
class BasicMaze:
    def __init__(self, x_lim, y_lim, origin=(1, 1), target=(None, None)):
        # 迷宫大小
        self.x_lim: int = x_lim
        self.y_lim: int = y_lim
        # 起点、终点
        self.origin: tuple[int, int] = origin
        if target[0] is None and target[1] is None:
            self.target: tuple[int, int] = (x_lim - 2, y_lim - 2)
        else:
            self.target: tuple[int, int] = target

        # 方向
        self.directions: list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # 格子情况，True表示有障碍物，False表示没有障碍物
        self.single = [[True for _ in range(y_lim)] for _ in range(x_lim)]

        # 记录是否被访问过
        self.visited = [[False for _ in range(y_lim)] for _ in range(x_lim)]

    def reset_visited(self):
        self.visited = [[False for _ in range(self.y_lim)] for _ in range(self.x_lim)]
    # 检查一个位置是否在迷宫内
    def is_valid_position(self, x, y):
        return 0 <= x < self.x_lim and 0 <= y < self.y_lim
    
    # 检查一个位置是否有障碍物
    def is_wall(self, x, y):
        return self.single[x][y]

    # 检查一个位置是否是通道
    def is_passage(self, x, y):
        return not self.single[x][y]
    
    # 检查一个位置是否已经被访问过
    def is_visited(self, x, y):
        return self.visited[x][y] if self.is_valid_position(x, y) else True

    # 标记一个位置为已访问
    def mark_visited(self, x, y):
        if self.is_valid_position(x, y):
            self.visited[x][y] = True

    # 随机选择起点终点，可选
    def choose_start_and_end(self):
        start_x = random.randint(0, self.x_lim - 1)
        start_y = random.randint(0, self.y_lim - 1)
        end_x = random.randint(0, self.x_lim - 1)
        end_y = random.randint(0, self.y_lim - 1)
        while start_x == end_x and start_y == end_y:
            end_x = random.randint(0, self.x_lim - 1)
            end_y = random.randint(0, self.y_lim - 1)
        self.origin = (start_x, start_y)
        self.target = (end_x, end_y)
        return (start_x, start_y), (end_x, end_y)
    
    def find_surround(self, x, y):
        surround = []
        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if self.is_valid_position(nx, ny) and not self.is_visited(nx, ny):
                surround.append((nx, ny))
        return surround
    
    # 打印迷宫
    def print_maze(self):
        for i in range(self.x_lim):
            for j in range(self.y_lim):
                if self.single[i][j]:
                    print('#', end='')
                else:
                    print(' ', end='')
            print()

# 第二种表达方式，墙壁不占位，只有通道占
# class BasicMaze2:
#     def __init__(self, size, origin=(0, 0), target=(None, None)):
#         # 迷宫大小
#         self.size = size
#         # 起点、终点
#         self.origin = origin
#         self.target = target
#         if target[0] is None and target[1] is None:
#             self.target = (size - 1, size - 1)
#         else:
#             self.target = target
#
#         # 方向
#         self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#
#         # 连通情况
#         self.connected = []  # 需要在这里初始化
#         self.visited = [[False for _ in range(size)] for _ in range(size)]
#
#     # 检查一个位置是否在迷宫内
#     def is_valid_position(self, x, y):
#         return 0 <= x < self.size and 0 <= y < self.size
#
#     # 检查一个位置是否有障碍物
#     def is_wall(self, x, y):
#         return not (x, y) in self.connected
#
#     # 检查一个位置是否是通道
#     def is_passage(self, x, y):
#         return (x, y) in self.connected
#
#     # 检查一个位置是否已经被访问过
#     def is_visited(self, x, y):
#         return self.visited[x][y] if self.is_valid_position(x, y) else True
#
#     # 随机选择起点终点，可选
#     def choose_start_and_end(self):
#         start_x = random.randint(0, self.size - 1)
#         start_y = random.randint(0, self.size - 1)
#         end_x = random.randint(0, self.size - 1)
#         end_y = random.randint(0, self.size - 1)
#         while start_x == end_x and start_y == end_y:
#             end_x = random.randint(0, self.size - 1)
#             end_y = random.randint(0, self.size - 1)
#         self.origin = (start_x, start_y)
#         self.target = (end_x, end_y)
#         return (start_x, start_y), (end_x, end_y)
#
#     # 打印迷宫
#     def print_maze(self):
#         pass