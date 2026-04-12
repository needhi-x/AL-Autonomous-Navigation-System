import matplotlib.pyplot as plt

def plot_grid(grid, path, start, goal):
    plt.imshow(grid, cmap='gray_r')

    y, x = zip(*path)
    plt.plot(x, y)

    plt.scatter(start[1], start[0], marker='o')
    plt.scatter(goal[1], goal[0], marker='x')

    plt.title("Autonomous Navigation Path")
    plt.show()