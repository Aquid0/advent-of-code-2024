import os

script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, "test.txt")
input_file_path = os.path.join(script_dir, "input.txt")

import re 

def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip() for l in tests]
    ans = 0 
    m = len(tests)
    n = len(tests[0])
    
    for r in range(m):
        for c in range(n):
            if tests[r][c] == 'X':
                if r+3 < m:
                    if tests[r+1][c] == 'M' and tests[r+2][c] == 'A' and tests[r+3][c] == 'S':
                        ans += 1
                if r-3 > -1:
                    if tests[r-1][c] == 'M' and tests[r-2][c] == 'A' and tests[r-3][c] == 'S':
                        ans += 1
                if c+3 < n:
                    if tests[r][c+1] == 'M' and tests[r][c+2] == 'A' and tests[r][c+3] == 'S':
                        ans += 1
                if c-3 > -1:
                    if tests[r][c-1] == 'M' and tests[r][c-2] == 'A' and tests[r][c-3] == 'S':
                        ans += 1
                if r + 3 < m and c + 3 < n:
                    if tests[r+1][c+1] == 'M' and tests[r+2][c+2] == 'A' and tests[r+3][c+3] == 'S':
                        ans += 1
                if r - 3 > -1 and c + 3 < n :
                    if tests[r-1][c+1] == 'M' and tests[r-2][c+2] == 'A' and tests[r-3][c+3] == 'S':
                        ans += 1
                if r + 3 < m and c - 3 > -1:
                    if tests[r+1][c-1] == 'M' and tests[r+2][c-2] == 'A' and tests[r+3][c-3] == 'S':
                        ans += 1
                if r - 3 > -1 and c - 3 > -1:     
                    if tests[r-1][c-1] == 'M' and tests[r-2][c-2] == 'A' and tests[r-3][c-3] == 'S':
                        ans += 1
    return ans
        
    

print(f"Test Solution: {solve(test_file_path)}")
print(f"Question Solution: {solve(input_file_path)}")
