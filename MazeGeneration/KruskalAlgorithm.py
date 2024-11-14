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

def generate(rows, columns):
    result = BasicMaze(rows, columns)
    uf = UnionFind(rows * columns)

    edges = []
    for i in range(rows * columns):
        for neighbor in result.find_surround(i):
            if i > neighbor:  # Avoid duplicate edges
                edges.append((i, neighbor))

    random.shuffle(edges)

    for u, v in edges:
        if not uf.connected(u, v):
            uf.union(u, v)
            x = u // columns
            y = u % columns
            result.single[x][y] = False

    return result

if __name__ == '__main__':
    m,n = 20,20
    i = BasicMaze(m,n)
    maze = generate(i)
    maze.show()