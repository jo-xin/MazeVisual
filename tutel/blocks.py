# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:44
# @Author  : jo-xin
# @File    : blocks.py

from os.path import join
from ursina import Entity, Button, scene, color, Sky
from ursina import load_texture


from tutel.entrance import application as app

application = app


def name_to_rel(name: str) -> str:
    return join("texture", name)


class TextureLib:
    light_blue_concrete = load_texture(name_to_rel("light_blue_concrete.png"))
    line_concrete = load_texture(name_to_rel("lime_concrete.png"))

    sunset_sky = load_texture(name_to_rel("sunset.jpeg"))


class Block(Button):
    def __init__(self, position=(0, 0, 0), texture=TextureLib.line_concrete):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            highlight_color=color.lime,
            color=color.white,
            texture=texture,
            origin_y=0.5
        )



