# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/11/16 23:01
# @Author  : jo-xin
# @File    : link_start.py
import time
from typing import Callable
from queue import Queue

import MazeGeneration
import MazeSolution
import tutel
import Maze_base

from ursina import application, held_keys, Entity


class Glue:
    @staticmethod
    def dfs(x_lim: int, y_lim: int) -> Maze_base.BasicMaze:
        maze: Maze_base.BasicMaze = Maze_base.BasicMaze(x_lim, y_lim)
        MazeGeneration.Dfs.generate(x_lim,y_lim)
        return maze

    @staticmethod
    def aco(maze: Maze_base.BasicMaze, gb_only=False) -> Queue:
        ant_num = 2
        max_round = 5
        decay_r = 0.3
        path = Queue()
        aco = MazeSolution.ACO.ACO(ant_num, maze, max_round, decay_r, path)
        gb, _ = aco.aco_maze()
        if gb_only:
            path = Queue()
        for n in gb:
            path.put(n)
        return path

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
    Dfs: Callable[[int, int], Maze_base.BasicMaze] = MazeGeneration.Dfs.generate
    KruskalAlgorithm: Callable[[int, int], Maze_base.BasicMaze] = MazeGeneration.KruskalAlgorithm.generate
    PrimAlgorithm: Callable[[int, int], Maze_base.BasicMaze] = MazeGeneration.PrimAlgorithm.generate
    RecursiveDivision: Callable[[int, int], Maze_base.BasicMaze] = MazeGeneration.RecursiveDivision.generate


class SolvingMethod:
    ACO: Callable[[Maze_base.BasicMaze], Queue] = lambda maze: Glue.aco(maze)
    AStar: Callable[[Maze_base.BasicMaze], Queue] = lambda maze: Glue.lit(maze, MazeSolution.AStar.AStar_sol)
    Bfs: Callable[[Maze_base.BasicMaze], Queue] = lambda maze: Glue.lit(maze, MazeSolution.Bfs.bfs_sol)
    Dfs: Callable[[Maze_base.BasicMaze], Queue] = lambda maze: Glue.lit(maze, MazeSolution.Dfs.dfs_sol)


class Sequel:
    def __init__(self, maze: Maze_base.BasicMaze):
        self.__ruinswald = maze
        self.__oldwald = Glue.disenchant(maze)
        self.__path: Queue = Queue()
        self.__world = tutel.New_World.MazeArtOnline(self.__oldwald)

    def __run(self):
        tutel.New_World.application.run()

    def stop(self):
        from ursina import application
        application.running = False

    def solve(self, dfs=False, bfs=False, astar=False, aco=False):
        if dfs:
            path = SolvingMethod.Dfs(self.__ruinswald)
            self.__path = tutel.water.SPELLCARD_SupremeGoodIsLikeWater(path, True, True)
        elif bfs:
            self.__path = SolvingMethod.Bfs(self.__ruinswald)
        elif astar:
            self.__path = SolvingMethod.AStar(self.__ruinswald)
        elif aco:
            self.__path = SolvingMethod.ACO(self.__ruinswald)
        else:
            raise ValueError("Solver not selected")

    def sktCoat(self, smooth_criminal=True, show_maze=False):
        if self.__path.empty():
            raise ValueError("The path is empty. Try SOLVEing the maze")

        if not show_maze:
            gp = Glue.aco(self.__ruinswald, True)

            self.__path.put((-100, -100))
            while not gp.empty():
                self.__path.put(gp.get())

        tutel.New_World.UnlimitedMazeWorks.UMW_camera_static(self.__oldwald)
        tutel.New_World.UnlimitedMazeWorks.UMW_ball_walk(self.__path, smooth_criminal)

        self.__run()

    def minecraft(self):
        if self.__path.empty():
            raise ValueError("The path is empty. Try SOLVEing the maze")

        tutel.New_World.UnlimitedMazeWorks.UMW_camera_walk(self.__path)

        self.__run()

    def player(self):
        tutel.New_World.UnlimitedMazeWorks.UMW_player(self.__ruinswald.origin)

        self.__run()

sequel: Sequel | None = None


def update():
    tutel.New_World.UnlimitedMazeWorks.update()
    if tutel.New_World.UnlimitedMazeWorks.m_walker is not None:
        sequel._Sequel__world.the_world.visit(tutel.New_World.UnlimitedMazeWorks.m_walker.object.object.position)


    if held_keys['q']:
        application.quit()





def test_minecraft():
    global sequel
    maze = GeneratingMethod.PrimAlgorithm(7, 7)

    sequel = Sequel(maze)
    sequel.solve(dfs=True)
    sequel.minecraft()


def test_sky01():
    global sequel
    maze = GeneratingMethod.PrimAlgorithm(15, 15)

    sequel = Sequel(maze)
    sequel.solve(aco=True)
    sequel.sktCoat(False)

def test_sky02():
    global sequel
    maze = GeneratingMethod.PrimAlgorithm(7, 7)

    sequel = Sequel(maze)
    sequel.solve(astar=True)
    sequel.sktCoat(False)

def test_player():
    global sequel

    sequel = Sequel(GeneratingMethod.PrimAlgorithm(10, 10))
    sequel.player()


def show_maze(maze: Maze_base.BasicMaze):
    global sequel

    sequel = Sequel(maze)
    sequel._Sequel__path.put(maze.origin)
    sequel.sktCoat(False, True)


if __name__ == '__main__':
    test_sky02()


