import math
from typing import List, Optional, Tuple


BLACK: Tuple[int, int, int] = (0, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
GREEN: Tuple[int, int, int] = (0, 255, 0)
RED  : Tuple[int, int, int] = (255, 0, 0)
BLUE : Tuple[int, int, int] = (0, 0, 255)

WIDTH : int = 30
HEIGHT: int= 30
STROK_WIDTH = int((math.sqrt(WIDTH) + math.sqrt(HEIGHT)) * 0.5)


WINDOW_WIDTH : int = WIDTH * 10 + 1
WINDOW_HEIGHT: int = HEIGHT * 10


 

COLS: int = (WINDOW_WIDTH) // WIDTH
ROWS: int = WINDOW_HEIGHT // HEIGHT

WINDOW_SIZE: Tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT + 5)

INIFINITY = 2**100