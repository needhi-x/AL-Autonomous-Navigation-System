from src.environment import create_grid
from src.planner import astar
from src.agent import move_agent
from src.visualization import plot_grid

def main():
    grid, start, goal = create_grid()

    print("Start:", start)
    print("Goal:", goal)

    path = astar(grid, start, goal)

    if path:
        print("\nPath Found!")
        print(path)

        move_agent(grid, path)
        plot_grid(grid, path, start, goal)
    else:
        print("No Path Found")

if __name__ == "__main__":
    main()