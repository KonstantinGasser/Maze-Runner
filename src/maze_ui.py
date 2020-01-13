import pygame
import random
import sys
from typing import List, Optional, Tuple

from constants import BLACK, WHITE, GREEN, RED, BLUE, WINDOW_SIZE, COLS, ROWS, WIDTH, HEIGHT 
from maze import MazeCreator, Node
from a_star_solver import AStar


CLOCK = pygame.time.Clock()

class Screen():
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption('Maze your way out')
        CLOCK.tick(60)
    
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
        pygame.draw.ellipse(
                            self.screen,
                            colr,
                            [
                                (i * WIDTH + int(WIDTH * 0.25)) ,
                                (j * HEIGHT + int(HEIGHT * 0.25)),
                                int(WIDTH / 2),
                                int(HEIGHT / 2),
                            ]
                        )
    

    def show_grid(self, grid):

        for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(1)
        self.screen.fill(BLACK)
        for i in range(ROWS):
            for j in range(COLS):
                walls = grid[i][j].get_walls()
                self.show_grid_node(walls)
                if grid[i][j].is_start:
                    self.show_rect(grid[i][j].i, grid[i][j].j, BLUE)
                if grid[i][j].is_end:
                    self.show_rect(grid[i][j].i, grid[i][j].j, RED)
        self._render_screen()

    def _render_screen(self):
        pygame.display.update()
        



def run() -> None:
    screen    = Screen()
    maze      = MazeCreator(screen)
    maze_grid = maze.create_maze()
    a_star    = AStar(screen, maze_grid)
    path      = a_star.a_star()

    
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)




if __name__  == '__main__':
    pygame.init()
    run()