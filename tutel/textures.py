# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:44
# @Author  : jo-xin
# @File    : textures.py

from ursina import Entity
from ursina import load_texture
from tutel import entrance


class TextureLib:
    light_blue_concrete = load_texture(".\\texture\\light_blue_concrete.png")



application = entrance.application



if __name__ == '__main__':
    cube = Entity(model="cube", scale=(4, 4, 4), texture=TextureLib.light_blue_concrete)
    application.run()