import numpy as np

def create_grid(size=10):
    grid = np.zeros((size, size))

    # Obstacles
    grid[3:7, 5] = 1
    grid[6, 2:6] = 1

    start = (0, 0)
    goal = (9, 9)

    return grid, start, goal