# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:02
# @Author  : jo-xin
# @File    : New_World.py
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from tutel import blocks, camera


BLOCKS = (blocks.TextureLib.line_concrete, blocks.TextureLib.orange_glass, blocks.TextureLib.light_blue_concrete)
# Set up the grid of blocks
height = 1
for y in range(0, height):
    for z in range(-15, 16):
        for x in range(-15, 16):
            blocks.Block(position=(x, y, z), texture=BLOCKS[(x+z)%3])

# Add sky to the scene
sky = Sky()

main_camera = camera.Camera()
main_camera.camera.position = Vec3(0, 1, -16)

for i in range(20):
    walking_duration = 0.9
    revolving_duration = 0.1

    main_camera.position.append(camera.Step(Vec3(0, 0, 1), walking_duration))
    main_camera.position.append(camera.Step(Vec3(0, 0, 0), revolving_duration))

    main_camera.rotation.append(camera.Step(Vec3(0, 0, 0), walking_duration))
    main_camera.rotation.append(camera.Step(Vec3(0, 90, 0), revolving_duration))

def update():
    global main_camera
    main_camera.update()

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