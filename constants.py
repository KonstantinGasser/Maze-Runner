from typing import List, Optional, Tuple

BLACK: Tuple[int, int, int] = (0, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
GREEN: Tuple[int, int, int] = (0, 255, 0)
RED  : Tuple[int, int, int] = (255, 0, 0)
BLUE : Tuple[int, int, int] = (0, 0, 255)
 
WINDOW_WIDTH : int = 900
WINDOW_HEIGHT: int = 800

WIDTH : int = 25
HEIGHT: int= 25
 

COLS: int = (WINDOW_WIDTH-100) // WIDTH
ROWS: int = WINDOW_HEIGHT // HEIGHT

WINDOW_SIZE: Tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT + 5)