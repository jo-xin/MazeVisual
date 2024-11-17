import sys
sys.path.append('..')
from Maze_base import BasicMaze
import random


# def check_passage(maze, new_x, new_y, current_dx, current_dy):
#     for dx, dy in maze.directions:
#         if dx+new_x == current_dx and dy+new_y == current_dy:
#             continue
#         next_x, next_y = new_x + dx, new_y + dy
#         if maze.is_visited(next_x, next_y):
#             return False
#     return True

# def dfs(maze, x, y):
#     # 标记当前位置为已访问
#     maze.mark_visited(x, y)
#     # 随机选择一个方向
#     directions = random.sample(maze.directions, len(maze.directions))
#     for dx, dy in directions:
#         new_x, new_y = x + dx, y + dy
#         # 如果新位置有效
#         if maze.is_valid_position(new_x, new_y) and not maze.is_visited(new_x, new_y):
#             if check_passage(maze,new_x,new_y,x,y):
#                 # 打通墙
#                 maze.single[new_x][new_y] = False
#                 dfs(maze, new_x, new_y)

# def generate(maze):
#     origin = maze.origin
#     target = maze.target
#     maze.visited[origin[0]][origin[1]]=True
#     sys.setrecursionlimit(maze.x_lim*maze.y_lim)  # 将默认的递归深度修改为3000
#     dfs(maze,origin[0],origin[1])
#     maze.single[origin[0]][origin[1]]=False
#     maze.visited[target[0]][target[1]] = True
#     maze.single[target[0]][target[1]] = False
#     maze.visited = [[False for _ in range(maze.x_lim)] for _ in range(maze.y_lim)]

def generate(x,y):
    rows = x // 2
    columns = y // 2
    White, Gray, Black = 0, 1, 2
    result = BasicMaze(rows, columns)
    color = [White] * (rows * columns)
    current = []
    color[0] = Gray
    current.append(0)
    connected = []
    while current:
        last = current[-1]
        neighbors = result.find_surround(last // columns, last % columns)
        random.shuffle(neighbors)
        for neighbor in neighbors:
            neighbor = neighbor[0] * columns + neighbor[1]
            if color[neighbor] == White:
                color[neighbor] = Gray
                connected.append((last,neighbor))
                current.append(neighbor)
                break
        else:  # No unvisited neighbors
            current.pop()
            color[last] = Black

    fi = BasicMaze(2*rows+1,2*columns+1)
    fi.single = [[False]*(2*columns+1) for _ in range(2*rows+1)]
    for i in range(rows):
        fi.single[2*i] = [True]*(2*columns+1)
    fi.single[2*rows] = [True]*(2*columns+1)
    for i in range(columns):
        for j in range(rows):
            fi.single[2*j+1][2*i] = True
            fi.single[2*j+1][2*columns] = True
    for u, v in connected:
        x1, y1 = divmod(u, columns)
        x2, y2 = divmod(v, columns)
        fi.single[x1+1+x2][y1+1+y2] = False
    return fi

if __name__ == '__main__':
    maze = generate(15,10)
    maze.print_maze()