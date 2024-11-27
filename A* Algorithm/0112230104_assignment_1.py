import math
import heapq

def heuristic(x, y, gx, gy):
    return math.sqrt((x - gx) ** 2 + (y - gy) ** 2)

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return path[::-1]

def get_neighbors(current, grid, directions):
    x, y = current
    rows, cols = len(grid), len(grid[0])
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1:
            neighbors.append((nx, ny))

    return neighbors

def a_star(grid, start, goal):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    open_list = [(0, start)]                                #heap
    cost_to_reach = {start: grid[start[0]][start[1]]}       #each node cost
    path_tracker = {}                                       #parent child track

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            
            return cost_to_reach[goal], reconstruct_path(path_tracker, start, goal)

        for neighbor in get_neighbors(current, grid, directions):
            nx, ny = neighbor
            new_cost = cost_to_reach[current] + grid[nx][ny]
            if neighbor not in cost_to_reach or new_cost < cost_to_reach[neighbor]:
                cost_to_reach[neighbor] = new_cost
                f_cost = new_cost + heuristic(nx, ny, *goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                path_tracker[neighbor] = current
    return float('inf'), [] 

if __name__ == "__main__":
    size = int(input("Enter the size of the grid: "))
    grid = []
    print("Enter the grid elements row-wise (space-separated):")
    for i in range(size):
        row = list(map(int, input().split()))
        grid.append(row)
            
    
    start = tuple(map(int, input("Enter the start coordinates (row col): ").split()))
    goal = tuple(map(int, input("Enter the goal coordinates (row col): ").split())) 
    
    cost, path = a_star(grid, start, goal)
    print("Optimal Cost:", cost)
    print("Optimal Path:", "-->".join(map(str, path)))
