import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def simulate_guard(grid, start, m, n):
    r,c = start 
    direction = 0 
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    
    while 0 <= r < m and 0 <= c < n:
        visited.add((r, c))
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc
        
        if not (0 <= nr < m and 0 <= nc < n):
            return visited
        elif grid[nr][nc] == "#": 
            direction = (direction + 1) % 4
        else:
            r, c = nr, nc


def check_loop(grid, start, m, n, obstruction):
    r, c = obstruction
    grid[r][c] = "#"  

    direction = 0 
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    seen = set()

    r, c = start
    while 0 <= r < m and 0 <= c < n:
        state = (r, c, direction)
        if state in seen:
            return True  
        seen.add(state)

        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < m and 0 <= nc < n):
            return False
        elif grid[nr][nc] == "#":
            direction = (direction + 1) % 4
        else:
            r, c = nr, nc

    return False


def solve(filename):
    with open(filename, 'r') as f:
        grid = f.readlines()
    grid = [list(l.strip()) for l in grid]
    m, n = len(grid), len(grid[0])
    start = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "^":
                start = (r, c)
                break
    
    visited = simulate_guard(grid, start, m, n)
    
    loops = set()
    
    for r, c in visited:
        if (r, c) != start:
            grid_copy = [row[:] for row in grid]
            if check_loop(grid_copy, start, m, n, (r,c)):
                loops.add((r, c))

    return len(loops)


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')