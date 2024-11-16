# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:02
# @Author  : jo-xin
# @File    : New_World.py
import queue

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from dataclasses import dataclass

from tutel import blocks, cameras, walker, water


@dataclass(frozen=True)
class MaZe:
    x_lim: int
    z_lim: int
    isWall: list[list[bool]]
    begging: tuple[int, int]
    ending: tuple[int, int]


class MazeArtOnline:
    def __init__(self, maze: MaZe, wall_height: int = 2, kabe_height: int = 3):
        self.the_world = blocks.ZaWarudo(maze.x_lim, maze.z_lim, wall_height, kabe_height)
        Sky()

        self.initialize_maze(maze)

    def initialize_maze(self, maze: MaZe):
        for x in range(maze.x_lim):
            for z in range(maze.z_lim):
                if maze.isWall[x][z]:
                    self.the_world.build_wall((x, z))
                else:
                    self.the_world.build_ground((x, z))

        self.the_world.build_beginning(maze.begging)
        self.the_world.build_ending(maze.ending)


class UnlimitedMazeWorks:
    m_walker = None

    def __init__(self):
        pass

    @classmethod
    def update_void(cls):
        return

    @classmethod
    def update_walk(cls):
        cls.m_walker.walk()

    update = update_void

    @classmethod
    def UMW_camera_walk(cls, path: queue.Queue):
        UnlimitedMazeWorks.m_walker = walker.AnWalker(cameras.Camera(65), path, 1.5)
        UnlimitedMazeWorks.m_walker.set_config(0.4, 0.2, 0.1)
        UnlimitedMazeWorks.m_walker.ghostPath()

        UnlimitedMazeWorks.update = UnlimitedMazeWorks.update_walk

    @classmethod
    def UMW_camera_static(cls, maze: MaZe):
        c_x = (maze.x_lim - 1) / 2
        c_z = (maze.z_lim - 1) / 2
        c_y = max(maze.z_lim * 20 / 8, maze.x_lim * 20 / 12)
        camera.position = Vec3(c_x, c_y, c_z)
        camera.rotation = Vec3(90, 0, 0)

    @classmethod
    def UMW_ball_walk(cls, path: queue.Queue):
        UnlimitedMazeWorks.m_walker = walker.AnWalker(
            cameras.MovingObject(Entity(model='sphere', color=color.red, scale=0.7)), path)
        UnlimitedMazeWorks.m_walker.set_config(0.1, 0, 0.05)
        UnlimitedMazeWorks.m_walker.ghostPath()

        UnlimitedMazeWorks.update = UnlimitedMazeWorks.update_walk




application = blocks.application

import Maze_base
# import MazeGeneration.PrimAlgorithm as pa
#
# maze = pa.generate(24, 12)
# mm = MaZe(24, 12, maze.single, maze.origin, maze.target)
# www = MazeArtOnline(mm)
#
# import MazeSolution.Dfs as ds
#
# history = queue.Queue()
# ds.dfs_sol(maze, history)
#
# # print(history.queue)
# # print(mm.ending)
# history = water.SPELLCARD_SupremeGoodIsLikeWater(history, True, True)
# # print(history.queue)
#
# UnlimitedMazeWorks.UMW_camera_static(mm)
# UnlimitedMazeWorks.UMW_ball_walk(history)


# UnlimitedMazeWorks.UMW_camera_walk(history)


# player = FirstPersonController()

