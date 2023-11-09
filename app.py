import numpy as np
import random
import matplotlib.pyplot as plt
from queue import Queue

# Define the maze size
maze_size = (100, 100)

# Create the maze with random walls
maze = np.zeros(maze_size, dtype=int)
for i in range(maze_size[0]):
    for j in range(maze_size[1]):
        if random.random() < 0.3:
            maze[i][j] = 1

# Define the start and end points
start = (0, 0)
end = (maze_size[0] - 1, maze_size[1] - 1)

# Define the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# Define the function to check if a move is valid
def is_valid_move(pos):
    return 0 <= pos[0] < maze_size[0] and pos[1] >= 0 and pos[1] < maze_size[1] and maze[pos[0]][pos[1]] == 0


# Define the function to solve the maze using BFS
def solve_maze():
    q = Queue()
    q.put(start)
    visited = set()
    parent = {}
    while not q.empty():
        curr = q.get()
        if curr == end:
            break
        for move in moves:
            next_pos = (curr[0] + move[0], curr[1] + move[1])
            if is_valid_move(next_pos) and next_pos not in visited:
                q.put(next_pos)
                visited.add(next_pos)
                parent[next_pos] = curr
    if end not in parent:
        return None
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    path.reverse()
    return path


# Solve the maze
path = solve_maze()

# Visualize the maze and the path
plt.imshow(maze, cmap='gray')
if path is not None:
    for i in range(len(path) - 1):
        plt.plot([path[i][1], path[i + 1][1]], [path[i][0], path[i + 1][0]], color='red')
else:
    plt.plot([start[1], end[1]], [start[0], end[0]], color='red')
plt.show()
