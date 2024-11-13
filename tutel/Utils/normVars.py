# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/11/7 19:19
# @Author  : jo-xin
# @File    : normVars.py


from os.path import dirname, basename, realpath, join
from sys import argv


class VARS:
    BASE_FOLDER_NAME = "MazeVisual"
    TEXTURE_REL_PATH = join("tutel", "texture")

    BASE_DIR = dirname(realpath(argv[0]))

    while basename(BASE_DIR) != BASE_FOLDER_NAME:
        BASE_DIR = dirname(BASE_DIR)

    TEXTURE_DIR = join(BASE_DIR, TEXTURE_REL_PATH)


