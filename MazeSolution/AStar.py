import queue
from Maze_base import BasicMaze

def get_h(x:int,y:int,target):
    return abs(x-target[0])+abs(y-target[1])

def AStar(maze:BasicMaze, x:int,y:int,dist:int,que:queue.PriorityQueue,history:queue.Queue):
    if x == maze.target[0] and y == maze.target[1]:
        return dist, True
    for dx,dy in maze.directions:
        next_x = x+dx
        next_y = y+dy
        if maze.is_valid_position(next_x,next_y):
            # print(next_x,next_y)
            if not maze.is_visited(next_x,next_y) and not maze.is_wall(next_x,next_y):
                maze.visited[next_x][next_y]=True
                # add history
                if history is not None:
                    history.put((next_x, next_y))
                que.put((dist+get_h(next_x,next_y,maze.target),next_x,next_y,dist+1))
    return dist, False


def AStar_sol(maze:BasicMaze,history:queue.Queue=None):
    que = queue.PriorityQueue()
    x = maze.origin[0]
    y = maze.origin[1]
    que.put((1+get_h(x,y,maze.target),x,y, 1))
    if history is not None:
        history.put((x,y))
    flag = False
    ans = 0
    while not flag:
        _, x, y, dist = que.get()
        ans, flag = AStar(maze, x, y, dist, que, history)
        if flag or que.empty():
            break
    maze.reset_visited()
    if flag:
        return ans
    else:
        return -1
