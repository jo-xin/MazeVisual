# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/11/14 16:11
# @Author  : jo-xin
# @File    : walker.py
import queue
from ursina import *

from tutel import camera


class AnWalker:
    def __init__(self, cam: camera.Camera, path: queue.Queue[tuple[int, int]], camera_height=1):
        self.current_position: Vec3 = Vec3(0, 0, 0)
        self.current_rotation: Vec3 = Vec3(0, 0, 0)

        self.block_duration = 0.9
        self.rest_duration = 0.1
        self.revolve_duration = 0.0 * self.block_duration + self.rest_duration
        self.WAKING_DURATION = 1

        self.camera_height = camera_height
        self.camera: camera.Camera = cam

        self.path: queue.Queue[Vec3] = queue.Queue()
        self.initilizeCamera(path.get())
        while not path.empty():
            x, z = path.get()
            self.path.put(Vec3(x, self.camera_height, z))

    def set_config(self, block=-1, rest=-1, revolve=-1):
        """
        set values to -1 will make it not changed
        """
        block = self.block_duration if block == -1 else block
        rest = self.rest_duration if rest == -1 else rest
        revolve = self.revolve_duration if revolve == -1 else revolve
        if min(block, rest, revolve) < 0.05:
            raise ValueError("duration set in set_config() is too short!")
        self.block_duration = block
        self.rest_duration = rest
        self.revolve_duration = revolve

    def ghostPath(self):
        self.shakeIt()
        while not self.path.empty():
            self.shake()

    def shakeIt(self):
        self.camera.position.append(camera.Step(duration=self.WAKING_DURATION))
        self.camera.rotation.append(camera.Step(duration=self.WAKING_DURATION))
        for i in range(10):
            self.camera.position.append(camera.Step(duration=self.WAKING_DURATION / 10))
            self.camera.rotation.append(camera.Step(duration=self.WAKING_DURATION / 10))

        self.camera.position.append(camera.Step(duration=self.revolve_duration))

    def shake(self):
        target = self.path.get()
        delta_position = self.delta_position(target)
        self.camera.position.append(camera.Step(delta_position, self.block_duration))
        if self.rest_duration != 0:
            self.camera.position.append(camera.Step(Vec3(0, 0, 0), self.rest_duration))

        self.camera.rotation.append(
            camera.Step(self.delta_rotation(self.x_to_theta(delta_position)), self.revolve_duration))
        self.camera.rotation.append(
            camera.Step(Vec3(0, 0, 0), self.block_duration + self.rest_duration - self.revolve_duration))

    def sheiku(self):
        self.camera.position.append(camera.Step(duration=self.WAKING_DURATION))
        self.camera.rotation.append(camera.Step(duration=self.WAKING_DURATION))

    def initilizeCamera(self, start: tuple[int, int]):
        self.current_position = Vec3(start[0], self.camera_height, start[1])
        self.camera.camera.position = self.current_position

        self.current_rotation = Vec3(90, 0, 0)
        self.camera.camera.rotation = self.current_rotation

    def walk(self):
        self.camera.update()

    def delta_position(self, position: Vec3) -> Vec3:
        delta = position - self.current_position
        self.current_position = position
        return delta

    def delta_rotation(self, rotation: Vec3) -> Vec3:
        delta = rotation - self.current_rotation
        self.current_rotation = rotation
        return delta

    @staticmethod
    def x_to_theta(dx: Vec3) -> Vec3:
        rotate = Vec3(0, 0, 0)
        if dx.x > 0:
            rotate.y = 90
        elif dx.x < 0:
            rotate.y = 270
        elif dx.z < 0:
            rotate.y = 180
        return rotate
