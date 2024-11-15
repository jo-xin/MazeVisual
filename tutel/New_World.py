# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:02
# @Author  : jo-xin
# @File    : New_World.py
import queue

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from tutel import blocks, camera, walker

BLOCKS = (blocks.TextureLib.line_concrete, blocks.TextureLib.orange_glass, blocks.TextureLib.light_blue_concrete)

bb = [[0 for _ in range(40)] for _ in range(40)]

# Set up the grid of blocks
height = 1
for y in range(0, height):
    for z in range(-15, 16):
        for x in range(-15, 16):
            bb[x + 15][z + 15] = blocks.Block(position=(x, y, z), texture=BLOCKS[(x + z) % 3])

for y in range(0, height):
    for z in range(-1, 2):
        for x in range(-1, 2):
            bb[x + 15][z + 15].enabled = False
            blocks.Block(position=(x, y, z), texture=blocks.TextureLib.quartz_block_bottom)


# Add sky to the scene
sky = Sky()
player = FirstPersonController()


"""
Here is An WAlker
"""

# q = queue.Queue()
# q.put((1, 1))
# q.put((1, 2))
# # q.put((1, 3))
# # q.put((2, 3))
# # q.put((2, 4))
# # q.put((2, 5))
# # q.put((1, 5))
# # q.put((1, 4))
# # q.put((1, 3))
# # q.put((1, 2))
#
# mm_walker = walker.AnWalker(camera.Camera(), q)
# # mm_walker.set_config()
# mm_walker.ghostPath()
#
#
# def update():
#     mm_walker.walk()


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


blocks.application.run()
