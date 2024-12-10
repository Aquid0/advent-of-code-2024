import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def solve(filename):
    with open(filename, 'r') as f:
        grid = f.readlines()
    grid = [l.strip() for l in grid]
    m = len(grid)
    n = len(grid[0])
    
    global score
    score = 0
    
    
    def f(curr_score, r, c, visited):
        global score
       
        if (r,c) in visited:
            return 0
       
        val = int(grid[r][c])
       
        if val == 9:
            score += 1
       
        visited.add((r, c))
       
        if r + 1 < m and grid[r+1][c] == str(val+1): f(curr_score, r+1, c, visited)
        if r - 1 > -1 and grid[r-1][c] == str(val+1): f(curr_score, r-1, c, visited)
        if c + 1 < n and grid[r][c+1] == str(val+1): f(curr_score, r, c+1, visited)
        if c - 1 > -1 and grid[r][c-1] == str(val+1): f(curr_score, r, c-1, visited)
        return 0
    
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "0":
                visited = set()
                f(0, r, c, visited)
                
    return score


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')