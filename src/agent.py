import time

def move_agent(grid, path):
    print("\nAgent Movement:\n")
    for step in path:
        print(f"Moving to {step}")
        time.sleep(0.3)