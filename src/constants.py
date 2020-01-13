from typing import List, Optional, Tuple

BLACK: Tuple[int, int, int] = (0, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
GREEN: Tuple[int, int, int] = (0, 255, 0)
RED  : Tuple[int, int, int] = (255, 0, 0)
BLUE : Tuple[int, int, int] = (0, 0, 255)
 
WINDOW_WIDTH : int = 500
WINDOW_HEIGHT: int = 500

WIDTH : int = 45
HEIGHT: int= 45
 

COLS: int = (WINDOW_WIDTH) // WIDTH
ROWS: int = WINDOW_HEIGHT // HEIGHT

WINDOW_SIZE: Tuple[int, int] = (WINDOW_WIDTH, WINDOW_HEIGHT + 5)