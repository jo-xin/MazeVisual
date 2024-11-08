# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:44
# @Author  : jo-xin
# @File    : textures.py

from os.path import join
from ursina import Entity
from ursina import load_texture

from tutel.entrance import application as app


def name_to_rel(name: str) -> str:
    return join("texture", name)


class TextureLib:
    light_blue_concrete = load_texture(name_to_rel("light_blue_concrete.png"))
    line_concrete = load_texture(name_to_rel("lime_concrete.png"))


application = app

if __name__ == '__main__':
    cube = Entity(model="cube", scale=(4, 4, 4), texture=TextureLib.line_concrete)
    application.run()
