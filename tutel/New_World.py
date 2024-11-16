# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:02
# @Author  : jo-xin
# @File    : New_World.py
import queue

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from dataclasses import dataclass

from tutel import blocks, camera, walker, water


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
        UnlimitedMazeWorks.m_walker = walker.AnWalker(camera.Camera(65), path, 1.5)
        UnlimitedMazeWorks.m_walker.set_config(0.4, 0.2, 0.1)
        UnlimitedMazeWorks.m_walker.ghostPath()

        UnlimitedMazeWorks.update = UnlimitedMazeWorks.update_walk


application = blocks.application

import Maze_base
import MazeGeneration.PrimAlgorithm as pa

maze = pa.generate(7, 7)
mm = MaZe(7, 7, maze.single, maze.origin, maze.target)
www = MazeArtOnline(mm)

import MazeSolution.Dfs as ds

history = queue.Queue()
ds.dfs_sol(maze, history)

# print(history.queue)
# print(mm.ending)
history = water.SPELLCARD_SupremeGoodIsLikeWater(history, True, True)
# print(history.queue)

UnlimitedMazeWorks.UMW_camera_walk(history)



# Add sky to the scene
# player = FirstPersonController()


"""
Here is An WAlker
"""

# q = queue.Queue()
# q.put((1, 1))
# q.put((1, 2))
# q.put((1, 3))
# q.put((2, 3))
# q.put((2, 4))
# q.put((2, 5))
# q.put((1, 5))
# q.put((1, 4))
# q.put((1, 3))
# q.put((1, 2))

# mm_walker = walker.AnWalker(camera.Camera(), q)
# # mm_walker.set_config()
# mm_walker.ghostPath()

# mmm = UnlimitedMazeWorks()
# mmm.UMW_camera_walk(q)



#
#
def update():
    UnlimitedMazeWorks.update()


#
# # Set the initial camera position and movement parameters
# camera.position = Vec3(0, 1, -16)  # Starting position
# target_position = Vec3(0, 1, -15)  # First target position (1 block forward)
# step_distance = 1  # Distance for each step forward
# move_speed = 2  # Speed of movement (higher = faster)
# moving = False  # Flag to indicate if the camera is currently moving
#
# # Create the moving object (a ball) using Entity
# ball = Entity(model='sphere', position=camera.position + Vec3(0, 0, 1), color=color.red, scale=0.5)
#
#
# # Function to set the next target position and start moving
# def set_next_target():
#     global target_position, moving
#     if camera.position.z < 0:  # Limit movement to 16 steps forward
#         target_position = camera.position + Vec3(0, 0, step_distance)
#         moving = True
#     else:
#         moving = False  # Stop moving once the target is reached
#
#
# # Update function to move the camera and the ball smoothly toward the target
# def update():
#     global moving
#     if moving:
#         # Move the camera toward the target position, with a speed of `move_speed`
#         camera.position = lerp(camera.position, target_position, time.dt * move_speed)
#
#         # Move the ball in front of the camera by updating its position relative to the camera
#         ball.position = camera.position + Vec3(0, 0, 5)  # 1 block in front of the camera
#
#         # Check if the camera is close enough to the target to stop moving
#         if distance(camera.position, target_position) < 0.05:
#             camera.position = target_position  # Snap to target to prevent overshooting
#             moving = False  # Stop movement
#             invoke(set_next_target, delay=0.5)  # Set the next target after a delay
#
#
# # Start the movement
# set_next_target()

application.run()

