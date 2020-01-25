from typing import List, Optional, Tuple
from constants import INIFINITY, COLS, ROWS, WIDTH, HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT

class Node():
    def __init__(self, i, j):
        self.i            = i
        self.j            = j
        self.visited      = False
        self.neighours    = []
        self.walls        = [True, True, True, True] #top , right, bottom, left
        self.center_point = self._compute_center(self.i, self.j)

        self.is_start     = False
        self.is_end       = False
        # for a* algo
        self.came_from    = None
        self.g_score      = INIFINITY
        self.f_score      = INIFINITY
        self.h_score      = 0
         


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
        if not self.walls[1] and self.index(self.i + 1, self.j) != -1:
            neighbors.append(grid[self.i + 1][self.j])
        if not self.walls[2] and self.index(self.i, self.j + 1) != -1:
            neighbors.append(grid[self.i][self.j + 1])
        if not self.walls[3] and self.index(self.i - 1, self.j) != -1:
            neighbors.append(grid[self.i - 1][self.j])

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
        elif i < self.i:
            self.walls[3] = False # remove right wall
        elif j > self.j:
            self.walls[2] = False # remove top wall
        elif j < self.j:
            self.walls[0] = False # remove bottom wall

    @staticmethod
    def _compute_center(i, j) -> Tuple[float, float]:
        if i == 0:
            tmp_x = 0
        else:
            tmp_x = WIDTH * i
        
        if j == 0:
            tmp_y = 0
        else:
            tmp_y = HEIGHT * j

        tmp_x = tmp_x + (WIDTH * 0.5)
        tmp_y = tmp_y + (HEIGHT * 0.5)
        return (tmp_x, tmp_y)


class Stack():
    def __init__(self):
        self.stack = []

    def add(self, obj) -> object:
        self.stack.append(obj)

    def pop(self) -> object:
        return self.stack.pop()
    
    def get_by_index(self, index) -> object:
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


    
# not yet sure where to use it
class TreeNode():
    def __init__(self, f_score, node):
        self.value      = f_score
        self.node_obj   = node
        self.left       = None
        self.right      = None

    def add_node(self, value, node) -> None:
        if node and value :
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value, node)
                else:
                    self.left.add_node(value, node)
            elif value > self.value:
                if self.right is None:
                    self.right = TreeNode(value, node)
                else:
                    self.right.add_node(value, node)
    
    def delete_node(self, root, obj):
        if not root: return root

        if obj < root.value:
            root.left  = self.delete_node(root.left, obj)
        elif obj > root.value:
            root.right = self.delete_node(root.right, obj)
        else:
            if not root.left: 
                return root.right
            elif not root.right:
                return root.left
            
            root.value = self.get_lowest_value(root.right)
            root.right = self.delete_node(root.right, root.value)
        return root
        
    def search_obj(self, obj) -> bool:
        if obj < self.value:
            if self.left is None:
                return False
            else:
                self.left.search_obj(obj)
        elif obj > self.value:
            if self.right is None:
                return None
            else: 
                self.right.search_obj(obj)
        else:
            return self.node
    
    def get_lowest_value(self, node=None):
        if not node.left:
            return node
        return node.get_lowest_value(node.left)
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()
    
    def get_tree_size(self, count_left, count_right):
        pass