# 没debug 也许能用?
import random


def check_passage(maze, new_x, new_y, current_dx, current_dy):
    for dx, dy in maze.directions:
        if dx == current_dx and dy == current_dy:
            continue
        next_x, next_y = new_x + dx, new_y + dy
        if not maze.is_valid_position(next_x, next_y) or maze.is_visited(next_x, next_y):
            return False
    return True

def dfs(maze, x, y):
    # 标记当前位置为已访问
    maze.mark_visited(x, y)
    # 随机选择一个方向
    directions = random.sample(maze.directions, len(maze.directions))
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # 如果新位置有效、未访问且不是墙，则可以打通这个方向的墙
        if maze.is_valid_position(new_x, new_y) and not maze.is_visited(new_x, new_y) and not maze.is_wall(new_x,new_y):
            if check_passage(maze,new_x,new_y,x,y):
                # 打通墙
                maze.single[new_x][new_y] = False
                maze.dfs(new_x, new_y)

def generate(maze):
    origin = maze.origin
    dfs(maze,origin[0],origin[1])