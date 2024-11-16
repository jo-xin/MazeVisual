import sys
sys.path.append('..')
from Maze_base import BasicMaze
import random


def check_passage(maze, new_x, new_y, current_dx, current_dy):
    for dx, dy in maze.directions:
        if dx+new_x == current_dx and dy+new_y == current_dy:
            continue
        next_x, next_y = new_x + dx, new_y + dy
        if maze.is_visited(next_x, next_y):
            return False
    return True

def dfs(maze, x, y):
    # 标记当前位置为已访问
    maze.mark_visited(x, y)
    # 随机选择一个方向
    directions = random.sample(maze.directions, len(maze.directions))
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # 如果新位置有效
        if maze.is_valid_position(new_x, new_y) and not maze.is_visited(new_x, new_y):
            if check_passage(maze,new_x,new_y,x,y):
                # 打通墙
                maze.single[new_x][new_y] = False
                dfs(maze, new_x, new_y)

def generate(maze):
    origin = maze.origin
    target = maze.target
    maze.visited[origin[0]][origin[1]]=True
    sys.setrecursionlimit(maze.x_lim*maze.y_lim)  # 将默认的递归深度修改为3000
    dfs(maze,origin[0],origin[1])
    maze.single[origin[0]][origin[1]]=False
    maze.visited[target[0]][target[1]] = True
    maze.single[target[0]][target[1]] = False
    maze.visited = [[False for _ in range(maze.x_lim)] for _ in range(maze.y_lim)]

if __name__ == '__main__':
    maze = BasicMaze(10, 10)
    generate(maze)
    maze.print_maze()