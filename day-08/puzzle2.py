import os
from itertools import combinations

script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')



def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    grid = [l.strip() for l in tests]
    m = len(grid)
    n = len(grid[0])
    frequencies = {}
    antinodes = set()


    for r in range(m):
        for c in range(n):
            if grid[r][c] != ".":
                if grid[r][c] not in frequencies:
                    frequencies[grid[r][c]] = [(r, c)]
                else:
                    frequencies[grid[r][c]].append((r, c))
    
    
    for idxs in frequencies.values():
        pairs = list(combinations(idxs, 2))
        for p1, p2 in pairs:
            x1, y1 = p1
            x2, y2 = p2
            

            b_x_fac = backward_diff_x = x1-x2
            b_y_fac = backward_diff_y = y1-y2
            f_x_fac = forward_diff_x = x2-x1
            f_y_fac = forward_diff_y = y2-y1


            while (0 <= x1 + (forward_diff_x) < m) and (0 <= y1 + (forward_diff_y) < n):            
                antinodes.add((x1+(forward_diff_x), y1+(forward_diff_y)))          
                forward_diff_x += f_x_fac
                forward_diff_y += f_y_fac

            while (0 <= x2 + (backward_diff_x) < m) and (0 <= y2 + (backward_diff_y) < n):
                antinodes.add((x2+(backward_diff_x), y2+(backward_diff_y)))          
                backward_diff_x += b_x_fac
                backward_diff_y += b_y_fac


    return len(antinodes)


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')