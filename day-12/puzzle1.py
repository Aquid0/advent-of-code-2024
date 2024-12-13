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

    def perimeter_for_square(r, c, char):
        perimeter = 0       
        if (r + 1 < m and grid[r+1][c] != char) or r+1 >= m:
            perimeter += 1
        if (r - 1 > -1 and grid[r-1][c] != char) or r-1 <= -1: 
            perimeter += 1 
        if (c + 1 < n and grid[r][c+1] != char) or c+1 >= n:
            perimeter += 1
        if c - 1 > -1 and grid[r][c-1] != char or c-1 <= -1:
            perimeter += 1
        return perimeter
           
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
    for char, region_list in regions.items():
        for region in region_list:
            area = len(region)
            perimeter = sum(perimeter_for_square(r, c, char) for r, c in region)
            ans += area * perimeter
                
    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(question_file_path)}')