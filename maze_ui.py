import pygame
import random
import sys

from typing import List, Optional, Tuple

BLACK: Tuple[int, int, int] = (0, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
GREEN: Tuple[int, int, int] = (0, 255, 0)
RED  : Tuple[int, int, int] = (255, 0, 0)
BLUE : Tuple[int, int, int] = (0, 0, 255)
 
WINDOW_WIDTH : int = 900
WINDOW_HEIGHT: int = 800

WIDTH : int = 45
HEIGHT: int= 45
 

COLS: int = (WINDOW_WIDTH-100) // WIDTH
ROWS: int = WINDOW_HEIGHT // HEIGHT

WINDOW_SIZE: Tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT + 5)

CLOCK = pygame.time.Clock()


def run() -> None:
    
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Maze your way out')

    maze_done = False
    grid = [[Node(j, i) for i in range(ROWS)] for j in range(COLS)]
    
    grid[0][0].visited = True

    stack = Stack()
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
                choosen_one = random.choice(neighbours)
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


class Node():
    def __init__(self, i, j):
        self.i         = i
        self.j         = j
        self.visited   = False
        self.neighours = []
        self.walls     = [True, True, True, True] #top , right, bottom, left

    def get_neighbours(self, grid):

        top_index = self.index(self.i, self.j - 1)
        top = None
        if top_index != -1:
            top    = grid[top_index[0]][top_index[1]]

        right_index = self.index(self.i + 1, self.j)
        right = None
        if right_index != -1:
            right    = grid[right_index[0]][right_index[1]]

        bottom_index = self.index(self.i, self.j + 1)
        bottom = None
        if bottom_index != -1:
            bottom = grid[bottom_index[0]][bottom_index[1]]
        
        left_index = self.index(self.i - 1, self.j)
        left = None
        if left_index != -1:
            left   = grid[left_index[0]][left_index[1]]



        if top is not None and not top.visited:
            self.neighours.append(top)
        if right is not None and not right.visited:
            self.neighours.append(right)
        if bottom is not None and not bottom.visited:
            self.neighours.append(bottom)
        if left is not None and not left.visited:
            self.neighours.append(left)
        return self.neighours

    @staticmethod
    def index(i,j):
        if (i < 0 or j < 0 or i > COLS-1 or j > ROWS-1 ):
            return -1
        return i, j

    def show_rect(self, screen, colr):
        return pygame.draw.rect(
                                screen,
                                colr,
                                [WIDTH * self.i + 3, HEIGHT * self.j + 3,WIDTH - 6 , HEIGHT - 6])

    def show(self, screen):
        l = 0.0
        # top wall
        if self.walls[0]:
            start = ((self.i * WIDTH) + (WIDTH * l), (self.j * HEIGHT)) 
            end   = ((self.i * WIDTH) + WIDTH - (WIDTH * l), (self.j * HEIGHT))
            pygame.draw.line(
                                screen, 
                                WHITE, 
                                start, 
                                end,
                                2
                            )
        

        # left wall
        if self.walls[1]:
            start = ((self.i * WIDTH) + WIDTH , (self.j * HEIGHT) + (HEIGHT * l)) 
            end   = ((self.i * WIDTH) + WIDTH, (self.j * HEIGHT) +  HEIGHT - (HEIGHT * l))
            pygame.draw.line(
                                screen, 
                                WHITE, 
                                start, 
                                end,
                                2
                            )

        # bottom wall
        if self.walls[2]:
            start = ((self.i * WIDTH) + (WIDTH * l), (self.j * HEIGHT) + HEIGHT) 
            end   = ((self.i * WIDTH) + WIDTH - (WIDTH * l), (self.j * HEIGHT) + HEIGHT)
            pygame.draw.line(
                                screen, 
                                WHITE, 
                                start, 
                                end,
                                2
                            )

        # right wall
        if self.walls[3]:
            start = ((self.i * WIDTH) , (self.j * HEIGHT) + (HEIGHT * l)) 
            end   = ((self.i * WIDTH), (self.j * HEIGHT) + HEIGHT - (HEIGHT * l))
            pygame.draw.line(
                                screen, 
                                WHITE, 
                                start, 
                                end,
                                2
                            )
        
    
        
    def remove_wall(self, i, j):
        if i > self.i:
            self.walls[1] = False # remove right wall
        elif i < self.i: 
            self.walls[3] = False # remove left wall
        elif j > self.j:
            self.walls[2] = False # remove bottom wall
        elif j < self.j: 
            self.walls[0] = False # remove top wall 

class Stack():
    def __init__(self):
        self.stack = []
    
    def add(self, obj):
        self.stack.append(obj)
    
    def pop(self):
        return self.stack.pop()

    def has_next(self):
        if len(self.stack) > 0: return True
        return False

if __name__  == '__main__':
    pygame.init()
    run()






