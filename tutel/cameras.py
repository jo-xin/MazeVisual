# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/11/12 18:51
# @Author  : jo-xin
# @File    : cameras.py
import queue
import random
from dataclasses import dataclass
from ursina import *

from tutel import entrance

app = entrance.application

DEFAULT_DURATION = 0.5


@dataclass(frozen=True)
class Step:
    delta: Vec3 = Vec3(0, 0, 0)
    duration: float = DEFAULT_DURATION


class Stepper:
    def __init__(self, smooth_criminal):
        self.steps = queue.Queue()  # a queue for all following steps

        self.delta: Vec3 = Vec3(0, 0, 0)  # displacement for each tick
        self.ticks_ahead: int = 0  # ticks remained to finish this step
        self.target: Vec3 = Vec3(0, 0, 0)  # teh target position for this step
        self.walking: bool = False  # is walking currently

        self.ima = 0
        self.history = []

        self.smooth_criminal = smooth_criminal

    def append(self, step: Step):
        """
        append Step into the queue
        :param step: Step
        :return: None
        """
        self.steps.put(step)
        pass

    def next_tick(self, current_position: Vec3) -> Vec3:
        """
        get the position at next tick. Move to next step if this step ends
        :param current_position: current position
        :param randomError: if a random error would be used
        :return: camera's position at next tick
        """
        if not self.walking:
            # When not walking
            if not self.steps.empty():
                # When there are still steps waiting
                self.plan_next_step(current_position)
                return self.next_tick(current_position)
            else:
                return current_position

        if self.ticks_ahead > 0:
            self.ticks_ahead -= 1
            return current_position + (self.delta if self.smooth_criminal else Vec3(0, 0, 0))
        else:
            # When planned step is finished, setting to target to avoid micro error
            target = self.target
            current_position = target
            self.finish_step(current_position)
            return target

    def finish_step(self, current_position: Vec3):
        """
        When the step is finished, go to next step or stop walking
        :param current_position: current position
        :return: None
        """
        if self.steps.empty():
            self.walking = False
        else:
            self.plan_next_step(current_position)

    def plan_next_step(self, current_position: Vec3):
        """
        When finishing a step, initialize variables used when walking
        :param current_position: current position
        :return: None
        """
        step = self.steps.get()
        self.ima += step.duration
        self.history.append((self.ima, step.delta))
        # print(f"At {self.ima} doing {step.delta}")
        # print(time.dt)
        self.ticks_ahead = step.duration // time.dt
        self.delta = step.delta / self.ticks_ahead
        self.target = current_position + step.delta
        self.walking = True


class MovingObject:
    def __init__(self, object: Entity, smooth_criminal):
        self.position = Stepper(smooth_criminal)
        self.rotation = Stepper(smooth_criminal)

        self.object = object

    def update(self):
        self.next_position()
        self.next_rotation()

    def next_position(self):
        self.object.position = self.position.next_tick(self.object.position)

    def next_rotation(self):
        self.object.rotation = self.rotation.next_tick(self.object.rotation)


class Camera(MovingObject):
    def __init__(self, fov: float = 0):
        super().__init__(camera, True)
        self.object.fov += fov









