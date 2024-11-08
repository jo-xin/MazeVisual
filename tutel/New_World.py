# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:02
# @Author  : jo-xin
# @File    : New_World.py
from ursina import Sky
from ursina.prefabs.first_person_controller import FirstPersonController

import blocks

app = blocks.app


def test_for_ground():
    height = 1
    for y in range(0, height):
        for z in range(-15, 16):
            for x in range(-15, 16):
                print(f"Position:({x},{y},{z})")
                blocks.Block(position=(x, y, z))

    player = FirstPersonController()
    sky = Sky()

    app.run()


if __name__ == '__main__':
    test_for_ground()
