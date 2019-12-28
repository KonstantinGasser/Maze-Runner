import pygame
from constants import COLS, ROWS, WIDTH, HEIGHT, WHITE
from typing import List, Optional, Tuple

class Node():
    def __init__(self, i, j):
        self.i         = i
        self.j         = j
        self.visited   = False
        self.neighours = []
        self.walls     = [True, True, True, True] #top , right, bottom, left

    def get_neighbours(self, grid) -> List[object]:

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
    def index(i,j) -> Tuple[int, int]:
        if (i < 0 or j < 0 or i > COLS - 1 or j > ROWS - 1 ):
            return -1
        return (i, j)


    def show(self) -> List[Tuple[int, int]]:
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

    def pop(self) -> Node:
        return self.stack.pop()

    def has_next(self) -> bool:
        if len(self.stack) > 0: return True
        return False
