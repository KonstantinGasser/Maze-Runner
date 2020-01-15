import pygame
import sys
import time

from data_collections import Stack
from typing import List
from constants import GREEN, BLACK, RED, BLUE, WHITE


class AStar():
    def __init__(self, screen, maze):
        self.open_set   = Stack()
        self.closed_set = Stack()
        self.screen     = screen
        self.grid       = maze
        self.path       = []   
    
    def a_star(self) -> None:
        grid       = self.grid
        start_node = grid[0][0]
        end_node   = grid[-1][-1]
        current = None

        start_node.g_score = 0
        start_node.f_score = 0 #self.dist_euclidean((start_node.i, start_node.j), (end_node.i, end_node.j))
        self.open_set.add(start_node)
        
        while self.open_set.has_next():
            self.screen.show_grid(grid)
            best_f = 0
            for i in range(len(self.open_set.stack)):
                if self.open_set.get_by_index(i).f_score < self.open_set.get_by_index(best_f).f_score:
                    best_f = i
            current = self.open_set.get_by_index(best_f)

            if current == end_node:
                return current
            
            self.open_set.del_obj(current)
            self.closed_set.add(current)

            neighbors = current.get_possible_neigbors(grid)

            for n in neighbors:
                if not self.closed_set.has_obj(n):
                    tmp_g = current.g_score + self.dist_euclidean((current.i, current.j),(n.i, n.j))

                    if not self.open_set.has_obj(n):
                        self.open_set.add(n)
                    elif tmp_g >= n.g_score:
                        continue

                    n.g_score = tmp_g
                    n.h_score = self.dist_euclidean((n.i, n.j), (end_node.i, end_node.j))

                    n.f_score = n.g_score + n.h_score
                    n.came_from = current
            
            self.show_current_state(current)
            time.sleep(0.15)
        return -1
            
    
    def show_current_state(self, current):
        for node in self.open_set.stack:
                self.screen.show_rect(
                        node.i,
                        node.j,
                        BLUE
                    )
        for node in self.closed_set.stack:
            self.screen.show_rect(
                    node.i,
                    node.j,
                    RED
                )
        self.screen.show_rect(
                    current.i,
                    current.j,
                    GREEN
                )
        self.screen._render_screen()

    @staticmethod
    def dist_euclidean(x1_y1, x2_y2):
        return abs(x1_y1[0] - x2_y2[0]) + abs(x1_y1[1] - x2_y2[1])

