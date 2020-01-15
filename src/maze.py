import pygame
import random
import sys

from typing import List, Optional, Tuple
from data_collections import Node, Stack
from constants import COLS, ROWS, BLUE
# from maze_ui import Screen


class MazeCreator():
    def __init__(self, screen):
        self.screen = screen        

    def create_maze(self) -> List[List]:
        stack                  = Stack()
        grid                   = []
        for i in range(0, ROWS):
            x = []
            for j in range(0, COLS):
                x.append(Node(i,j))
            grid.append(x)
        grid[0][0].is_start = True
        grid[-1][-1].is_end = True

        maze_done              = False
        
        grid[0][0].visited     = True

        stack.add(grid[0][0])

        while not maze_done:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(1)
    
            if stack.has_next():
                current    = stack.pop()
                neighbours = [n for n in current.get_neighbors(grid) if not n.visited]
            
                if len(neighbours) > 0:
                    stack.add(current)

                    choosen_one         = random.choice(neighbours)
                    choosen_one.visited = True

                    stack.add(choosen_one)

                    current.remove_wall(choosen_one.i, choosen_one.j)
                    choosen_one.remove_wall(current.i, current.j)
                    
                    
                    self.screen.show_grid(grid)
                    self.screen.show_rect(
                        choosen_one.i,
                        choosen_one.j,
                        BLUE
                    )
                    self.screen._render_screen()
            else:
                maze_done = True
        return grid



    
        


