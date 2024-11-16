如果想要使用MazeSolution中的算法：
```python
from MazeSolution import Dfs
from MazeSolution import Bfs
from MazeSolution import AStar
from MazeSolution import ACO
# 假设已经生成了一个妹子

# ...

# BFS
max_len = Bfs.bfs_sol(maze)
print(max_len)
# DFS
max_len = Dfs.dfs_sol(maze)
print(max_len)
# A*
max_len = AStar.AStar_sol(maze)
print(max_len)
# ant colony
ant_num=10 # 蚂蚁数
max_round=5 # 搜寻轮数
decay_r=0.3 #信息素衰减率
# 剩下的q和ini_c分别是释放的信息素浓度和初始信息素浓度
# alpha、beta是寻找下一个点时的参数
ac=ACO.ACO(ant_num,maze,max_round,decay_r)
path,length=ac.aco_maze()
print(length)
# 注：history都是再展示的地方加
```