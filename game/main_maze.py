# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque

s = deque()


maze_csv_path = "labirinto1.txt"  # Substitua pelo caminho correto
maze = Maze() 

maze.load_from_csv(maze_csv_path)

# Exibir o lab
maze.run()
maze.init_player()

p = maze.get_init_pos_player()

maze.mov_player(p)
if maze.solve_with_stack():
    print("Caminho até o prêmio encontrado com sucesso!")
else:
    print("Não foi possível encontrar o prêmio.")

time.sleep(5)


