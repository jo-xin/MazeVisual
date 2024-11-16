import queue
from Maze_base import BasicMaze


def dfs(maze:BasicMaze,new_x:int,new_y:int,last_x:int,last_y:int,history:queue.Queue=None):
    max_length = maze.x_lim*maze.y_lim
    if new_x == maze.target[0] and new_y == maze.target[1]:
        history.put((new_x, new_y))
        # print("find target")
        # print(new_x,new_y)
        if history is not None:
            history.put((-1,-1)) # 找到了一个解
        return 1
    maze.visited[new_x][new_y] = True
    # add queue
    if history is not None:
        history.put((new_x,new_y))
    for dx,dy in maze.directions:
        if dx+new_x == last_x and dy+new_y == last_y:
            continue
        next_x = dx+new_x
        next_y = dy+new_y
        if maze.is_valid_position(next_x, next_y) and not maze.is_wall(next_x,next_y):
            if not maze.is_visited(next_x, next_y):
                max_length = min(max_length,dfs(maze,next_x,next_y,new_x,new_y,history))
    maze.visited[new_x][new_y] = False
    # add queue
    if history is not None:
        history.put((new_x,new_y))
    return max_length+1



def dfs_sol(maze:BasicMaze,history:queue.Queue=None):
    maze.visited[maze.origin[0]][maze.origin[1]] = True
    max_length = -1
    # add queue
    if history is not None:
        history.put(maze.origin)
    for dx, dy in maze.directions:
        next_x = dx + maze.origin[0]
        next_y = dy + maze.origin[1]
        if maze.is_valid_position(next_x, next_y) and not maze.is_wall(next_x, next_y):
            max_length = dfs(maze,next_x,next_y,maze.origin[0],maze.origin[1], history)
    maze.visited = [[False for _ in range(maze.x_lim)] for _ in range(maze.y_lim)]
    if max_length == maze.x_lim*maze.y_lim+1:
        max_length = -1
    return max_length+1