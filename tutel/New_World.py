# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:02
# @Author  : jo-xin
# @File    : New_World.py
from ursina import Entity

# import ursina
import textures



if __name__ == '__main__':
    app = textures.application
    cube = Entity(model="cube", scale=(4, 4, 4), texture=textures.TextureLib.light_blue_concrete)
    app.run()


