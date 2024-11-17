# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/11/16 23:01
# @Author  : jo-xin
# @File    : link_start.py

from typing import Callable
from queue import Queue

import MazeGeneration
import MazeSolution
import tutel
import Maze_base


class Glue:
    @staticmethod
    def dfs(x_lim: int, y_lim: int) -> Maze_base.BasicMaze:
        maze: Maze_base.BasicMaze = Maze_base.BasicMaze(x_lim, y_lim)
        MazeGeneration.Dfs.generate(maze)
        return maze

    @staticmethod
    def lit(maze: Maze_base.BasicMaze, solver: Callable[[Maze_base.BasicMaze, Queue], any]) -> Queue:
        path = Queue()
        solver(maze, path)
        return path

    @staticmethod
    def nie(maze: Maze_base.BasicMaze) -> Queue:
        raise NotImplementedError("Please contact administrator, or developer.")

    @staticmethod
    def disenchant(maze: Maze_base.BasicMaze) -> tutel.New_World.MaZe:
        return tutel.New_World.MaZe(maze.x_lim, maze.y_lim, maze.single, maze.origin, maze.target)


class GeneratingMethod:
    Dfs: Callable[[int, int], Maze_base.BasicMaze] = Glue.dfs
    KruskalAlgorithm: Callable[[int, int], Maze_base.BasicMaze] = MazeGeneration.KruskalAlgorithm.generate
    PrimAlgorithm: Callable[[int, int], Maze_base.BasicMaze] = MazeGeneration.PrimAlgorithm.generate
    RecursiveDivision: Callable[[int, int], Maze_base.BasicMaze] = MazeGeneration.RecursiveDivision.generate


class SolvingMethod:
    ACO: Callable[[Maze_base.BasicMaze], Queue] = Glue.nie
    AStar: Callable[[Maze_base.BasicMaze], Queue] = Glue.nie if True else lambda maze: Glue.lit(maze, MazeSolution.AStar.AStar_sol)
    Bfs: Callable[[Maze_base.BasicMaze], Queue] = Glue.nie if True else lambda maze: Glue.lit(maze, MazeSolution.Bfs.bfs_sol)
    Dfs: Callable[[Maze_base.BasicMaze], Queue] = lambda maze: Glue.lit(maze, MazeSolution.Dfs.dfs_sol)


class Sequel:
    def __init__(self, maze: Maze_base.BasicMaze):
        self.__ruinswald = maze
        self.__oldwald = Glue.disenchant(maze)
        self.__path: Queue = Queue()
        tutel.New_World.MazeArtOnline(self.__oldwald)

    def __run(self):
        tutel.New_World.application.run()

    def solve(self):
        pass

    def sktCoat(self, path: Queue):
        path = tutel.water.SPELLCARD_SupremeGoodIsLikeWater(path, True, True)
        tutel.New_World.UnlimitedMazeWorks.UMW_camera_static(self.__oldwald)
        tutel.New_World.UnlimitedMazeWorks.UMW_ball_walk(path)

        self.__run()

    def minecraft(self, path: Queue):
        path = tutel.water.SPELLCARD_SupremeGoodIsLikeWater(path, True, True)
        tutel.New_World.UnlimitedMazeWorks.UMW_camera_walk(path)

        self.__run()


def update():
    tutel.New_World.UnlimitedMazeWorks.update()


if __name__ == '__main__':
    maze = GeneratingMethod.PrimAlgorithm(10, 10)
    path = SolvingMethod.Bfs(maze)
    print(path.queue)
    sequel = Sequel(maze)
    sequel.sktCoat(path)
