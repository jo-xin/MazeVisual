from Maze_base import BasicMaze


def dfs(maze,new_x,new_y,last_x,last_y,queue=None):
    max_length = maze.x_lim*maze.y_lim
    if new_x == maze.target[0] and new_y == maze.target[1]:
        # print("find target")
        # print(new_x,new_y)
        return 1
    maze.visited[new_x][new_y] = True
    # add queue
    for dx,dy in maze.directions:
        if dx+new_x == last_x and dy+new_y == last_y:
            continue
        next_x = dx+new_x
        next_y = dy+new_y
        if maze.is_valid_position(next_x, next_y) and not maze.is_wall(next_x,next_y):
            if not maze.is_visited(next_x, next_y):
                max_length = min(max_length,dfs(maze,next_x,next_y,new_x,new_y,queue))
    maze.visited[new_x][new_y] = False
    # add queue
    return max_length+1



def dfs_sol(maze):
    maze.visited[maze.origin[0]][maze.origin[1]] = True
    max_length = -1
    # add queue
    for dx, dy in maze.directions:
        next_x = dx + maze.origin[0]
        next_y = dy + maze.origin[1]
        if maze.is_valid_position(next_x, next_y) and not maze.is_wall(next_x, next_y):
            max_length = dfs(maze,next_x,next_y,maze.origin[0],maze.origin[1])
    return max_length