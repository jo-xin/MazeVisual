# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/11/14 16:11
# @Author  : jo-xin
# @File    : walker.py
import queue
from ursina import *

from tutel import cameras


class AnWalker:
    def __init__(self, obj: cameras.MovingObject, path: queue.Queue[tuple[int, int]], height=1):
        self.current_position: Vec3 = Vec3(0, 0, 0)
        self.current_rotation: Vec3 = Vec3(0, 0, 0)

        self.block_duration = 0.9
        self.rest_duration = 0.1
        self.revolve_duration = 0.0 * self.block_duration + self.rest_duration
        self.WAKING_DURATION = 1

        self.height = height
        self.object: cameras.MovingObject = obj

        self.path: queue.Queue[Vec3] = queue.Queue()
        self.initilizeObject(path.get())
        while not path.empty():
            x, z = path.get()
            self.path.put(Vec3(x, self.height, z))

    def set_config(self, block=-1, rest=-1, revolve=-1):
        """
        set values to -1 will make it not changed
        """
        block = self.block_duration if block == -1 else block
        rest = self.rest_duration if rest == -1 else rest
        revolve = self.revolve_duration if revolve == -1 else revolve
        if min(block, revolve) < 0.02:
            raise ValueError("duration set in set_config() is too short!")
        self.block_duration = block
        self.rest_duration = rest
        self.revolve_duration = revolve

    def ghostPath(self):
        self.shakeIt()
        while not self.path.empty():
            self.shake()

    def shakeIt(self):
        self.object.position.append(cameras.Step(duration=self.WAKING_DURATION))
        self.object.rotation.append(cameras.Step(duration=self.WAKING_DURATION))
        for i in range(10):
            self.object.position.append(cameras.Step(duration=self.WAKING_DURATION / 10))
            self.object.rotation.append(cameras.Step(duration=self.WAKING_DURATION / 10))

        self.object.position.append(cameras.Step(duration=self.revolve_duration))

    def shake(self):
        target = self.path.get()
        delta_position = self.delta_position(target)
        self.object.position.append(cameras.Step(delta_position, self.block_duration))
        if self.rest_duration != 0:
            self.object.position.append(cameras.Step(Vec3(0, 0, 0), self.rest_duration))

        self.object.rotation.append(
            cameras.Step(self.delta_rotation(self.x_to_theta(delta_position)), self.revolve_duration))
        self.object.rotation.append(
            cameras.Step(Vec3(0, 0, 0), self.block_duration + self.rest_duration - self.revolve_duration))

    def sheiku(self):
        self.object.position.append(cameras.Step(duration=self.WAKING_DURATION))
        self.object.rotation.append(cameras.Step(duration=self.WAKING_DURATION))

    def initilizeObject(self, start: tuple[int, int]):
        self.current_position = Vec3(start[0], self.height, start[1])
        self.object.object.position = self.current_position

        self.current_rotation = Vec3(90, 0, 0)
        self.object.object.rotation = self.current_rotation

    def walk(self):
        self.object.update()

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
