import pygame
import random
import sys
from typing import List, Optional, Tuple

from constants import BLACK, WHITE, GREEN, RED, BLUE, WINDOW_SIZE, COLS, ROWS, WIDTH, HEIGHT
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
            



INIFINITY = 2**100
class Node():
    def __init__(self, i, j):
        self.i         = i
        self.j         = j
        self.visited   = False
        self.neighours = []
        self.walls     = [True, True, True, True] #top , right, bottom, left
        
        self.is_start = False
        self.is_end   = False
        # for a* algo
        self.came_from = None
        self.g_score = INIFINITY
        self.f_score = INIFINITY
        self.h_score = 0


    def get_neighbors(self, grid) -> List[object]:

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

    def get_possible_neigbors(self, grid) -> List[object]: #TODO indexOutOfBounds
        neighbors = []
        if not self.walls[0] and self.index(self.i, self.j - 1) != -1:
            neighbors.append(grid[self.i][self.j - 1])
            print('NO TOP WALL')
        if not self.walls[1] and self.index(self.i + 1, self.j) != -1:
            neighbors.append(grid[self.i + 1][self.j])
            print('NO RIGHT WALL')
        if not self.walls[2] and self.index(self.i, self.j + 1) != -1:
            neighbors.append(grid[self.i][self.j + 1])
            print('NO BOTTOM WALL')
        if not self.walls[3] and self.index(self.i - 1, self.j) != -1:
            neighbors.append(grid[self.i - 1][self.j])
            print('NO LEFT WALL')
        
        for n in neighbors:
            print(f'I:{n.i}; J:{n.j}')
            print(f'Current walls:{self.walls}')
        return neighbors

    @staticmethod
    def index(i,j) -> Tuple[int, int]:
        if (i < 0 or j < 0 or i > COLS - 1 or j > ROWS - 1):
            return -1
        return (i, j)

    def get_walls(self) -> List[Tuple[int, int]]:
        walls_to_draw = []
        l = 0.0
        # top wall
        if self.walls[0]:
            start = ((self.i * WIDTH) + (WIDTH * l), (self.j * HEIGHT))
            end   = ((self.i * WIDTH) + WIDTH - (WIDTH * l), (self.j * HEIGHT))
            walls_to_draw.append((start, end))

        # left wall
        if self.walls[1]:
            start = ((self.i * WIDTH) + WIDTH , (self.j * HEIGHT) + (HEIGHT * l))
            end   = ((self.i * WIDTH) + WIDTH, (self.j * HEIGHT) +  HEIGHT - (HEIGHT * l))
            walls_to_draw.append((start, end))

        # bottom wall
        if self.walls[2]:
            start = ((self.i * WIDTH) + (WIDTH * l), (self.j * HEIGHT) + HEIGHT)
            end   = ((self.i * WIDTH) + WIDTH - (WIDTH * l), (self.j * HEIGHT) + HEIGHT)
            walls_to_draw.append((start, end))

        # right wall
        if self.walls[3]:
            start = ((self.i * WIDTH) , (self.j * HEIGHT) + (HEIGHT * l))
            end   = ((self.i * WIDTH), (self.j * HEIGHT) + HEIGHT - (HEIGHT * l))
            walls_to_draw.append((start, end))

        return walls_to_draw


    def remove_wall(self, i, j) -> None:
        if i > self.i:
            self.walls[1] = False # remove left wall
            print('REMOVE LEFT WALL')
        elif i < self.i:
            self.walls[3] = False # remove right wall
            print('REMOVE RIGHT WALL')
        elif j > self.j:
            self.walls[2] = False # remove top wall
            print('REMOVE TOP WALL')
        elif j < self.j:
            self.walls[0] = False # remove bottom wall
            print('REMOVE BOTTOM WALL')

class Stack():
    def __init__(self):
        self.stack = []

    def add(self, obj) -> None:
        self.stack.append(obj)

    def pop(self) -> Node:
        return self.stack.pop()
    
    def get_by_index(self, index) -> Node:
        return self.stack[index]

    def del_obj(self, obj) -> None:
        for item in self.stack: # next step change list with binary search tree 
            if item == obj:
                self.stack.remove(obj)
    
    def has_obj(self, obj) -> bool:
        for item in self.stack:
            if item == obj: return True
        return False

    def has_next(self) -> bool:
        if len(self.stack) > 0: return True
        return False


class Tree():
    def __init__(self, root):
        self.root = root
    
    def search_lowest(self, node) -> object:
        if node.left is None:
            return node.value
        return self.search_lowest(node.left)
    
    

    

class TreeNode():
    def __init__(self, f_score):
        self.value = f_score
        self.left  = None
        self.right = None

    def add_node(self, node) -> object:
        if node.value < self.value: # add as left child
            if self.left is None:
                self.left = node
                return
            else: return self.left.add_node(node)
        if node.value > self.value: # add as  right child
            if self.right is None:
                self.right = node
                return
            else: return self.right.add_node(node)
        
    def search_obj(self, obj) -> bool:
        if self.value == obj:
            return True
        if obj < self.value:
            return self.left.search_obj(obj)
        if obj > self.value:
            return self.right.search_obj(obj)

    
        


