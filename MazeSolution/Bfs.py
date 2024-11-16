import queue
from Maze_base import BasicMaze


def Bfs(maze:BasicMaze,que:queue.Queue,new_x:int,new_y:int,dist:int,history:queue.Queue=None):
    if new_x==maze.target[0] and new_y==maze.target[1]:
        return dist,True
    for dx,dy in maze.directions:
        next_x = new_x+dx
        next_y = new_y+dy
        if maze.is_valid_position(next_x,next_y):
            if not maze.is_visited(next_x,next_y) and not maze.is_wall(next_x,next_y):
                maze.visited[next_x][next_y] = True
                # add history
                if history is not None:
                    history.put((next_x,next_y))
                que.put((next_x,next_y,dist+1))
    return dist,False



def bfs_sol(maze:BasicMaze, history:queue.Queue=None):
    que = queue.Queue()
    origin = maze.origin
    que.put((origin[0],origin[1],1))
    if history is not None:
        history.put((origin[0],origin[1]))
    flag = False
    ans=0
    while not flag:
        x,y,dist=que.get()
        ans,flag=Bfs(maze,que,x,y,dist,history)
        if que.empty():
            break
    maze.reset_visited()
    if flag:
        return ans
    else:
        return -1
