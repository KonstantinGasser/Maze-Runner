import pygame
import random
import sys

from maze import Node, Stack

from typing import List, Optional, Tuple
from constants import BLACK, WHITE, GREEN, RED, BLUE, WINDOW_SIZE, COLS, ROWS, WIDTH, HEIGHT 

print(COLS)
CLOCK = pygame.time.Clock()

class Screen():
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.grid   = [[Node(j, i) for i in range(ROWS)] for j in range(COLS)]
        pygame.display.set_caption('Maze your way out')
    
    def show_grid_node(self, walls) -> None:
        for wall in walls:
            pygame.draw.line(
                                self.screen, 
                                WHITE, 
                                wall[0], 
                                wall[1],
                                2
                            )

    def show_rect(self, i, j, colr) -> None:
        pygame.draw.rect(
                            self.screen,
                            colr,
                            [
                                WIDTH * i,
                                HEIGHT * j,
                                WIDTH ,
                                HEIGHT
                            ]
                        )



def run() -> None:
    
    screen                 = Screen()
    grid                   = screen.grid
    stack                  = Stack()

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
            neighbours = [n for n in current.get_neighbours(grid) if not n.visited]
        
            if len(neighbours) > 0:
                stack.add(current)

                choosen_one         = random.choice(neighbours)
                choosen_one.visited = True

                stack.add(choosen_one)

                current.remove_wall(choosen_one.i, choosen_one.j)
                choosen_one.remove_wall(current.i, current.j)
                
                screen.screen.fill(BLACK)
                for i in range(ROWS):
                    for j in range(COLS):
                        walls = grid[i][j].show()
                        screen.show_grid_node(walls)
                
                screen.show_rect(
                    choosen_one.i,
                    choosen_one.j,
                    RED
                )

                screen.show_rect(
                    grid[0][0].i,
                    grid[0][0].j,
                    GREEN
                )

                screen.show_rect(
                    grid[-1][-1].i,
                    grid[-1][-1].j,
                    BLUE
                )
            
        CLOCK.tick(20)
        pygame.display.flip()


if __name__  == '__main__':
    pygame.init()
    run()