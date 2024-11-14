import sys
sys.path.append('..')
from Maze_base import BasicMaze
import random

def generate(bm) -> BasicMaze:
    bm.single = [[False for _ in range(bm.x_lim)] for _ in range(bm.y_lim)]
    bm.single[0] = [True for _ in range(bm.x_lim)]
    bm.single[-1] = [True for _ in range(bm.x_lim)]
    for i in range(bm.y_lim):
        bm.single[i][0] = True
        bm.single[i][-1] = True
    out = []
    divide(bm, 1, 1, bm.y_lim - 1, bm.x_lim - 1,out)
    return bm

def divide(list_obj: BasicMaze, left: int, top: int, right: int, bottom: int,out: list):
    if right - left < 4 and bottom - top < 4:  # 确保有足够的空间进行分割
        return

    elif right - left < 4:
        y = random.randint(top + 2, bottom - 2) if top + 2 < bottom - 2 else top + 2
        to_disconnect = [(i, y) for i in range(left, right + 1) if (i,y) not in out]
        if not [item for item in [(i, y) for i in range(left, right + 1)] if item in out]:
            gap_pos = random.randint(left + 1, right - 1) if left + 1 < right - 1 else left + 1
            p = gap_pos
            q = y
            to_disconnect.remove((p, q))
            out.append((p, q))
        for p, q in to_disconnect:
            list_obj.single[q][p] = True
        divide(list_obj, left, top, right, y,out)
        divide(list_obj, left, y, right, bottom,out)

    elif bottom - top < 4:
        x = random.randint(left + 2, right - 2) if left + 2 < right - 2 else left + 2
        to_disconnect = [(x, j) for j in range(top, bottom + 1) if (x,j) not in out]
        if not [item for item in [(x, j) for j in (top, bottom + 1)] if item in out]:
            gap_pos = random.randint(top + 1, bottom - 1) if top + 1 < bottom - 1 else top +1
            p = x
            q = gap_pos
            to_disconnect.remove((p, q))
            out.append((p, q))
        for p, q in to_disconnect:
            list_obj.single[q][p] = True 
        divide(list_obj, x, top, right, bottom,out)
        divide(list_obj, left, top, x, bottom,out)

    else:
        # 选择内部的x和y点进行分割（避免边界）
        x = random.randint(left + 2, right - 2) if left + 2 < right - 2 else left + 2
        y = random.randint(top + 2, bottom - 2) if top + 2 < bottom - 2 else top + 2

        # 确定要断开的连接
        to_disconnect = [(i, y) for i in range(left, right + 1) if (i,y) not in out] + \
                        [(x, j) for j in range(top, bottom + 1) if (x,j) not in out]

         # Determine the gap position
        position = random.randint(0, 3)
        gap_pos = [0] * 4
        gap_pos[0] = random.randint(top + 1, y - 1) if top + 1 < y - 1 else top + 1
        gap_pos[1] = random.randint(y + 1, bottom - 1) if y + 1 < bottom - 1 else y +1
        gap_pos[2] = random.randint(left + 1, x - 1) if left + 1 < x - 1 else left + 1
        gap_pos[3] = random.randint(x + 1, right - 1) if x + 1 < right - 1 else x + 1
        for i in range(4):
            if position != i:
                if i <= 1: # Gap is in top or bottom
                    p = x
                    q = gap_pos[i]
                else:  # Gap is in left or right
                    p = gap_pos[i]
                    q = y
                to_disconnect.remove((p, q))
                out.append((p, q))
        # 断开连接
        for p, q in to_disconnect:
            list_obj.single[q][p] = True

        # 递归分割四个区域
        divide(list_obj, left, top, x, y,out)
        divide(list_obj, x, top, right, y,out)
        divide(list_obj, left, y, x, bottom,out)
        divide(list_obj, x, y, right, bottom,out)

def show(list_obj: BasicMaze):
    for i in range(list_obj.y_lim):
        for j in range(list_obj.x_lim):
            if list_obj.single[i][j]:
                print('#', end='')
            else:
                print(' ', end='')
        print()

if __name__ == '__main__':
    m,n = 20,20
    i = BasicMaze(m,n)
    maze = generate(i)
    show(maze)