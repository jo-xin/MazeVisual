# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/10/30 11:44
# @Author  : jo-xin
# @File    : blocks.py

from os.path import join
from ursina import Entity, Button, scene, color, Sky, Vec3
from ursina import load_texture


from tutel.entrance import application as app

application = app


def name_to_rel(name: str) -> str:
    return join("texture", name)


class TextureLib:
    light_blue_concrete = load_texture(name_to_rel("light_blue_concrete.png"))
    line_concrete = load_texture(name_to_rel("lime_concrete.png"))
    orange_concrete = load_texture(name_to_rel("orange_concrete.png"))
    orange_glass = load_texture(name_to_rel("orange_stained_glass.png"))
    quartz_block_bottom = load_texture(name_to_rel("quartz_block_bottom.png"))
    stone = load_texture(name_to_rel("stone.png"))
    stone_bricks = load_texture(name_to_rel("stone_bricks.png"))

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



class ZaWarudo:
    BLOCK_GROUND = TextureLib.orange_glass
    BLOCK_WALL = TextureLib.stone_bricks
    BLOCK_KABE = TextureLib.stone
    BLOCK_BEGIN = TextureLib.line_concrete
    BLOCK_END = TextureLib.light_blue_concrete
    BLOCK_VISITED = TextureLib.orange_concrete
    BLOCK_FINISHED = TextureLib.quartz_block_bottom

    def __init__(self, x_lim, z_lim, wall_height=1, kabe_height=2):
        self.wall_height = wall_height
        self.kabe_height = kabe_height
        self.world: list[list[list[None | Block]]] = [[[None for _ in range(z_lim)] for _ in range(wall_height+1)] for _ in range(x_lim)]
        self.gp2 = False

        self.initialize_kabe(x_lim, z_lim)

    def initialize_kabe(self, x_lim, z_lim):
        for x in (-1, x_lim):
            for z in range(-1, z_lim + 1):
                self.build_kabe((x, z))

        for x in range(0, x_lim):
            for z in (-1, z_lim):
                self.build_kabe((x, z))

    def set_block(self, position: tuple[int, int, int], target: Block):
        x, y, z = position
        if (block := self.world[x][y][z]) is not None:
            block.enabled = False
        self.world[x][y][z] = target

    def visit(self, position: Vec3):
        x = round(position.x)
        z = round(position.z)
        if x + z < 0:
            self.gp2 = True
            return
        if (block := self.world[x][0][z]) is not None:
            if not self.gp2:
                if block.texture == self.BLOCK_GROUND:
                    self.set_block((x, 0, z), Block(position=(x, 0, z), texture=self.BLOCK_VISITED))
            else:
                self.set_block((x, 0, z), Block(position=(x, 0, z), texture=self.BLOCK_FINISHED))

    def build_ground(self, position: tuple[int, int]):
        self.set_block((position[0], 0, position[1]), Block(position=(position[0], 0, position[1]), texture=self.BLOCK_GROUND))

    def build_wall(self, position: tuple[int, int]):
        self.build_ground(position)
        for y in range(1, self.wall_height + 1):
            self.set_block((position[0], y, position[1]), Block(position=(position[0], y, position[1]), texture=self.BLOCK_WALL))

    def build_kabe(self, position: tuple[int, int]):
        Block(position=(position[0], 0, position[1]), texture=self.BLOCK_GROUND)
        for y in range(1, self.kabe_height + 1):
            Block(position=(position[0], y, position[1]), texture=self.BLOCK_KABE)

    def build_beginning(self, position: tuple[int, int]):
        self.set_block((position[0], 0, position[1]),
                       Block(position=(position[0], 0, position[1]), texture=self.BLOCK_BEGIN))

    def build_ending(self, position: tuple[int, int]):
        self.set_block((position[0], 0, position[1]),
                       Block(position=(position[0], 0, position[1]), texture=self.BLOCK_END))


