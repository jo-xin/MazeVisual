import queue

import numpy as np
import random
from Maze_base import BasicMaze


def get_h(x:int, y:int, target:tuple):
    return abs(x - target[0]) + abs(y - target[1])

class ACO:
    def __init__(self, ant_num:int, maze:BasicMaze, max_round:int, decay_r:float,q:int=1,ini_C:int=1):
        super().__init__()
        self.ant_num = ant_num
        self.maze = maze
        self.alpha = 1
        self.beta = 1
        self.max_round = max_round
        self.phe = np.zeros((maze.x_lim,maze.y_lim))
        self.phe += ini_C
        self.Q = q
        self.decay_rate = decay_r


# 更新信息素
    def update_phe(self, paths):
        for path in paths:
            for i in range(0, len(path)):
                # print(path[i])
                self.phe[path[i]] += self.Q / (len(path) - 1)
        self.phe *= (1 - self.decay_rate)


    # 选择下一个位置
    def choose_next(self,current):
        move_probs = []
        for dx,dy in self.maze.directions:
            next_x = current[0] + dx
            next_y = current[1] + dy
            if self.maze.is_valid_position(next_x,next_y) and not self.maze.is_wall(next_x,next_y):
                if not self.maze.is_visited(next_x,next_y):
                    di=get_h(next_x, next_y, self.maze.target)
                    if di == 0:
                        di=0.1
                    pheromone_level = self.phe[current[0]][current[1]] ** self.alpha * (1.0 / di) ** self.beta
                    move_probs.append(((next_x,next_y), pheromone_level))
        total_prob = sum(prob for _, prob in move_probs)
        r = random.uniform(0, total_prob)
        # print(move_probs)
        for pos, prob in move_probs:
            r -= prob
            if r <= 0:
                return pos



    def aco_maze(self,history:queue.Queue=None):
        best_path = None
        best_length = float('inf')
        for iteration in range(self.max_round):
            paths = []
            for ant in range(self.ant_num):
                if history is not None:
                    history.put((-1,-1))
                path = [self.maze.origin]
                if history is not None:
                    history.put(self.maze.origin)
                self.maze.visited[self.maze.origin[0]][self.maze.origin[1]]=True
                while path[-1] != self.maze.target:
                    next_pos = self.choose_next(path[-1])
                    if next_pos is not None:
                        if history is not None:
                            history.put(next_pos)
                    while next_pos is None:
                        path.pop()
                        next_pos = self.choose_next(path[-1])
                        if history is not None:
                            history.put(next_pos)
                    path.append(next_pos)
                    # print(next_pos[0])
                    self.maze.visited[next_pos[0]][next_pos[1]]=True
                    if next_pos == self.maze.target:
                        break
                if len(path) < best_length:
                    best_length = len(path)
                    best_path = path
                paths.append(path)
                self.maze.reset_visited()
            self.update_phe(paths)
            if history is not None:
                history.put("Update Pheromone")
        return best_path, best_length
