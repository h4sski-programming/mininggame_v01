CELL_SIZE:int = 32
WIDTH, HEIGHT = 1280, 720
FPS: int = 10
BG_COLOUR = (200, 200, 200)
SCORE_FONT_SIZE = CELL_SIZE


RESOLUTION = (WIDTH, HEIGHT)
RESOLUTION_MAIN = (WIDTH, HEIGHT - CELL_SIZE)

CELL_ROWS: int = RESOLUTION_MAIN[1] // CELL_SIZE
CELL_COLUMS: int = RESOLUTION_MAIN[0] // CELL_SIZE

SCORE_RECT = (0, CELL_ROWS * CELL_SIZE, RESOLUTION[0], RESOLUTION[1])