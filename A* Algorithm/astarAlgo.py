import math
from queue import PriorityQueue

def heuristic(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx + dy) + (math.sqrt(2) - 2) * min(dx, dy)

class State:
    def __init__(self, x, y, parent=None, g=0, h=0):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(grid, start, goal):
    open_set = PriorityQueue()
    closed_set = set()
    cost_so_far = {}

    start_node = State(start[0], start[1])
    start_node.g = 0
    start_node.h = heuristic(start, goal)
    open_set.put(start_node)
    cost_so_far[(start[0], start[1])] = 0

    while not open_set.empty():
        current_node = open_set.get()
        current_coords = (current_node.x, current_node.y)

        if current_coords == goal:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            path.reverse()
            return path, cost_so_far[goal]

        closed_set.add(current_coords)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            new_x, new_y = current_node.x + dx, current_node.y + dy
            new_coords = (new_x, new_y)

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != -1:

                move_cost = grid[new_x][new_y]
                if abs(dx) == abs(dy):
                    move_cost *= math.sqrt(2)

                new_cost = current_node.g + move_cost

                if new_coords not in cost_so_far or new_cost < cost_so_far[new_coords]:
                    cost_so_far[new_coords] = new_cost
                    new_node = State(new_x, new_y, current_node)
                    new_node.g = new_cost
                    new_node.h = heuristic((new_x, new_y), goal)
                    open_set.put(new_node)

    return None, None

if __name__ == "__main__":

    N = int(input("Enter the size of the grid (N): "))
    grid = []
    print("Enter the grid elements row-wise (space-separated):")
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)


    sx, sy = map(int, input("Enter the starting cell (Sx, Sy): ").split())
    dx, dy = map(int, input("Enter the destination cell (Dx, Dy): ").split())

    start = (sx, sy)
    goal = (dx, dy)

    path, cost = a_star_search(grid, start, goal)

    if path:
        print("Optimal Cost:", round(cost))
        print("Optimal Path:")
        for i in range(len(path) - 1):
            print(f"({path[i][0]},{path[i][1]})→({path[i+1][0]},{path[i+1][1]})")
    else:
        print("No path found.") 
