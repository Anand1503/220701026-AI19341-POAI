import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, end), 0, start))

    g_cost = {start: 0}
    came_from = {}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while open_list:
        _, current_g, current = heapq.heappop(open_list)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0):
                tentative_g = current_g + 1
                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g
                    f_cost = tentative_g + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f_cost, tentative_g, neighbor))
                    came_from[neighbor] = current

    return None

# Example usage
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)
print("Path found:", path)