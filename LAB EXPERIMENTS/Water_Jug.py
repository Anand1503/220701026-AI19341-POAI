def dfs(x, y, target, visited, path, a, b):
    if b == target:
        print("Solution found:")
        for step in path:
            print(step)
        return True
    if (a, b) in visited:
        return False
    visited.add((a, b))
    path.append(f"({a}, {b})")
    if dfs(x, y, target, visited, path, x, b):
        return True
    if dfs(x, y, target, visited, path, a, y):
        return True
    if dfs(x, y, target, visited, path, 0, b):
        return True
    if dfs(x, y, target, visited, path, a, 0):
        return True
    if a + b <= y:
        if dfs(x, y, target, visited, path, 0, a + b):
            return True
    else:
        if dfs(x, y, target, visited, path, a - (y - b), y):
            return True
    if a + b <= x:
        if dfs(x, y, target, visited, path, a + b, 0):
            return True
    else:
        if dfs(x, y, target, visited, path, x, b - (x - a)):
            return True
    path.pop()
    return False

def water_jug_dfs():
    x, y = 3, 4
    target = 2
    visited = set()
    path = []
    if not dfs(x, y, target, visited, path, 0, 0):
        print("No solution exists.")

water_jug_dfs()
