import pygame
import random
import sys

from maze import Node, Stack

from typing import List, Optional, Tuple
from constants import BLACK, WHITE, GREEN, RED, BLUE, WINDOW_SIZE, COLS, ROWS 

print(COLS)
CLOCK = pygame.time.Clock()

def _set_up_screen() -> pygame.Surface:
    pygame.display.set_caption('Maze your way out')
    return pygame.display.set_mode(WINDOW_SIZE)

def _set_up_grid() -> List[List[Node]]:
    return [[Node(j, i) for i in range(ROWS)] for j in range(COLS)]

def run() -> None:
    
    screen                 = _set_up_screen()
    stack                  = Stack()

    maze_done              = False
    grid                   = _set_up_grid() 
    
    grid[0][0].visited     = True

    stack.add(grid[0][0])

    while not maze_done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)
 
        if stack.has_next():
            current    = stack.pop()
            neighbours = [n for n in current.get_neighbours(grid) if not n.visited]
        
            if len(neighbours) > 0:
                stack.add(current)

                choosen_one         = random.choice(neighbours)
                choosen_one.visited = True

                stack.add(choosen_one)

                current.remove_wall(choosen_one.i, choosen_one.j)
                choosen_one.remove_wall(current.i, current.j)
                
                screen.fill(BLACK)
                for i in range(ROWS):
                    for j in range(COLS):
                        grid[i][j].show(screen)

                choosen_one.show_rect(screen, RED)
                
                grid[0][0].show_rect(screen, GREEN)
                grid[-1][-1].show_rect(screen, BLUE)
        CLOCK.tick(20)
        pygame.display.flip()


if __name__  == '__main__':
    pygame.init()
    run()






