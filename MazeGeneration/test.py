import sys
import random
sys.path.append('..')
from Maze_base import BasicMaze

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

def generate(x, y):
    rows = x // 2
    columns = y // 2
    uf = UnionFind(rows * columns)

    edges = []

    # 创建边的列表
    for i in range(rows):
        for j in range(columns):
            current_index = i * columns + j
            # 右邻居
            if j + 1 < columns:
                edges.append((current_index, current_index + 1))
            # 下邻居
            if i + 1 < rows:
                edges.append((current_index, current_index + columns))

    random.shuffle(edges)  # 随机打乱边的顺序

    # 创建最终的迷宫结构
    fi = BasicMaze(2 * rows + 1, 2 * columns + 1)

    # 初始化迷宫，设置墙壁
    for i in range(2 * rows + 1):
        for j in range(2 * columns + 1):
            fi.single[i][j] = True  # 默认设置为墙壁

    # 设置初始的墙壁
    for i in range(rows):
        fi.single[2 * i] = [True] * (2 * columns + 1)  # 横向墙壁

    for i in range(columns):
        for j in range(rows):
            fi.single[2 * j + 1][2 * i] = True  # 竖向墙壁

    # 使用 Kruskal 算法构建迷宫
    for u, v in edges:
        if not uf.connected(u, v):
            uf.union(u, v)

            # 计算通道位置
            x1, y1 = divmod(u, columns)
            x2, y2 = divmod(v, columns)

            # 开通通道
            fi.single[2 * x1 + 1][2 * y1 + 1] = False  # 开通通道
            fi.single[2 * x2 + 1][2 * y2 + 1] = False  # 开通通道
            fi.single[x1+1+x2][y1+1+y2] = False

    return fi

if __name__ == '__main__':
    maze = generate(20, 20)
    maze.print_maze()