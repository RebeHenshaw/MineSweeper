HEIGHT= 600
WIDTH = 800
GRID_SIZE = 6
CELL_COUNT = GRID_SIZE **2
MINES_COUNT = (CELL_COUNT) // 6

def height_prct(percentage):
    return (HEIGHT / 100) * percentage


def width_prct(percentage):
    return (WIDTH / 100) * percentage
