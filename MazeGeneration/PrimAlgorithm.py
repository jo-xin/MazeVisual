import sys
sys.path.append('..')
from Maze_base import BasicMaze
import random

def generate(x, y):
    rows = x // 2
    columns = y // 2
    result = BasicMaze(rows, columns)
    linked = [False] * (rows * columns)
    linked[0] = True
    paths = {(0, 1), (0, columns)}
    random.seed()  # Initialize random number generator
    connected = set()
    while paths:
        # Randomly select a path in paths
        pos = random.randint(0, len(paths) - 1)
        current_path = list(paths)[pos]
        # Connect the two nodes of the path
        connected.add((current_path[0], current_path[1]))
        # Determine which node is currently linked
        if not linked[current_path[0]]:
            current = current_path[0]
        else:
            current = current_path[1]
        # Add the node to linked
        linked[current] = True
        # Add all unvisited paths to paths and delete all invalid paths
        for neighbor in result.find_surround(current//columns, current%columns):
            neighbor = neighbor[0] * columns + neighbor[1]
            current_path = (min(neighbor, current), max(neighbor, current))
            if not linked[neighbor]:
                paths.add(current_path)
            else:
                paths.discard(current_path)

    fi = BasicMaze(2*rows+1,2*columns+1)
    fi.single = [[False]*(2*columns+1) for _ in range(2*rows+1)]
    for i in range(rows):
        fi.single[2*i] = [True]*(2*columns+1)
    fi.single[2*rows] = [True]*(2*columns+1)
    for i in range(columns):
        for j in range(rows):
            fi.single[2*j+1][2*i] = True
            fi.single[2*j+1][2*columns] = True
    for u, v in connected:
        x1, y1 = divmod(u, columns)
        x2, y2 = divmod(v, columns)
        fi.single[x1+1+x2][y1+1+y2] = False
    return fi

if __name__ == '__main__':
    maze = generate(19, 10)
    maze.print_maze()