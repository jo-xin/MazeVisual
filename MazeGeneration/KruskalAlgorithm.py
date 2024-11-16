import sys
sys.path.append('..')
from Maze_base import BasicMaze
import random
from collections import defaultdict

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

def generate(x,y):
    rows = x // 2
    columns = y // 2
    result = BasicMaze(rows, columns)
    uf = UnionFind(rows * columns)

    edges = []
    for i in range(rows * columns):
        x = i // columns
        y = i % columns
        for neighbor in result.find_surround(x,y):
            if i > neighbor[1]*columns + neighbor[0]:  # Avoid duplicate edges
                edges.append((i, neighbor[1]*columns + neighbor[0]))

    random.shuffle(edges)

    # for u, v in edges:
    #     if not uf.connected(u, v):
    #         uf.union(u, v)
    #         result.single[x][y] = False
    #         maze.single[u // columns][u % columns] = False
    #         maze.single[v // columns][v % columns] = False


    fi = BasicMaze(2*rows+1,2*columns+1)
    fi.single = [[False]*(2*columns+1) for _ in range(2*rows+1)]
    for i in range(rows):
        fi.single[2*i] = [True]*(2*columns+1)
    fi.single[2*rows] = [True]*(2*columns+1)
    for i in range(columns):
        for j in range(rows):
            fi.single[2*j+1][2*i] = True
            fi.single[2*j+1][2*columns] = True
    for u, v in edges:
        if not uf.connected(u, v):
            uf.union(u, v)
            x1, y1 = divmod(u, columns)
            x2, y2 = divmod(v, columns)
            fi.single[x1+1+x2][y1+1+y2] = False
    return fi

if __name__ == '__main__':
    maze = generate(15,11)
    maze.print_maze()