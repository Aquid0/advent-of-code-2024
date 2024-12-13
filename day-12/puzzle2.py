import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
question_file_path = os.path.join(script_dir, 'question.txt')


def solve(filename):
    with open(filename, 'r') as f:
        grid = f.readlines()
    grid = [l.strip() for l in grid]


    m = len(grid)
    n = len(grid[0])
    visited = set()
    regions = {} # character : [[idxs, idxs, idxs], [idxs]]
    
    
    def find_region(r, c, char, region):
        if (r, c) in visited:
            return 
        
        visited.add((r, c))
        region.add((r, c))
        
        if r + 1 < m and grid[r+1][c] == char:
            find_region(r+1, c, char, region)
        if r - 1 > -1 and grid[r-1][c] == char:
            find_region(r-1, c, char, region)
        if c + 1 < n and grid[r][c+1] == char:
            find_region(r, c+1, char, region)
        if c - 1 > -1 and grid[r][c-1] == char:
            find_region(r, c-1, char, region)     
        return region   
           
           
    def in_bounds(r, c, m, n):
        return -1 < r < m and -1 < c < n        
           
           
    for r in range(m):
        for c in range(n):
            char = grid[r][c]
            region = find_region(r, c, char, set())
            if char in regions:
                regions[char].append(region)
            else:
                regions[char] = [region]


    for char, region_list in regions.items():
        regions[char] = [r for r in region_list if r]
    

    ans = 0
    sides = 0
    for char, region_list in regions.items():
        for region in region_list:
            area = len(region)
            sides = 0
            for r, c in region:
                for i, j, adj_1, adj_2 in [
                (1, 1, (0, 1), (1, 0)),
                (1, -1, (0, -1), (1, 0)),
                (-1, 1, (0, 1), (-1, 0)),
                (-1, -1, (0, -1), (-1, 0)),
            ]:
                    dr, dc = (r+i, c+j)
                    adj_1 = (r + adj_1[0], c + adj_1[1])
                    adj_2 = (r + adj_2[0], c + adj_2[1])

                    is_diag_out = not in_bounds(dr,dc,m,n) or (dr, dc) not in region
                    is_adj_1_out = not in_bounds(adj_1[0],adj_1[1],m,n) or adj_1 not in region
                    is_adj_2_out = not in_bounds(adj_2[0],adj_2[0],m,n) or adj_2 not in region

                    sides += bool(
                        (is_diag_out and is_adj_1_out and is_adj_2_out)
                        or (is_diag_out and not is_adj_1_out and not is_adj_2_out)
                        or (not is_diag_out and is_adj_1_out and is_adj_2_out)
                    )
            ans += area * sides
    
    
    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(question_file_path)}')