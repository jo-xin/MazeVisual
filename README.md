大家早上好！！！

### 使い方：

例えば：

```python
global sequel
maze = GeneratingMethod.PrimAlgorithm(15, 15)
sequel = sequel(maze)
sequel.solve(astar=True)
sequel.minecraft()
```

第一行全局变量的声明，如果是在函数中（如例子的 test 系列函数）则需要加，否则就不需要加

第二行生成迷宫，输入 GeneratingMethod 再输入 . 之后，你的 IDE 应该就会告诉你有哪些可以用的方法，使用相应的方法，输入迷宫的长宽数据即可

第三行创建 Sequel 对象，输入迷宫

第四行解迷宫，在调用函数时将要用的解迷宫的方法名设置为 True 即可（你的 IDE 应该会告诉你有哪些写可用的方法）

第五行开始运行。使用 minecraft() 函数将以第一人称视角运行；
使用 skyCoat() 函数将在天上以俯瞰视角运行，
输入 True 会令小球平滑运动，在每两个格子之间平移过去，
输入 False 则会令小球"离散"的移动，每一格之间会瞬移。



