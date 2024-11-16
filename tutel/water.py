# -*- coding: utf-8 -*-
# @Project : MazeVisual
# @Time    : 2024/11/16 19:57
# @Author  : jo-xin
# @File    : water.py

from queue import Queue
from ursina import Vec2


def SPELLCARD_SupremeGoodIsLikeWater(queue: Queue[tuple[int, int]], back_after_1: bool, jumping: bool) -> Queue[tuple[int, int]]:
    """
    to handle problems existed in queue, BONDS Tier
    :param queue: queue that needs preprocessing
    :param back_after_1: There's a backward path from the ending to the beginning after a (-1, -1)
    :param jumping: There might be jumping over a block, which definitely appeared once before
    :return: preprocessed queue
    """
    path: list[tuple[int, int]] = []
    while not queue.empty():
        path.append(queue.get())

    if back_after_1:
        path = path[:path.index((-1, -1))]

    if jumping:
        path_: list[tuple[int, int]] = [path[0],]
        for i in range(1, len(path)):
            a = Vec2(path[i-1])
            b = Vec2(path[i])
            if (b - a).length() > 1:
                for point in path_:
                    c = Vec2(point)
                    if (c - a).length() == 1 and (c - b).length() == 1:
                        path_.append(point)
                        break

            path_.append(path[i])
        path = path_

    q: Queue[tuple[int, int]] = Queue()
    for n in path:
        q.put(n)
    return q



