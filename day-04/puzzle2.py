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
            if tests[r][c] == 'A':
                if r+1 < n and r-1 > -1 and c+1 < m and c-1 > -1: 
                    t1 = [tests[r+1][c+1], tests[r][c], tests[r-1][c-1]]
                    t2 = [tests[r+1][c-1], tests[r][c], tests[r-1][c+1]]
                    if (t1 == ['M', 'A', 'S'] or t1[::-1] == ['M', 'A', 'S']) and (t2 == ['M', 'A', 'S'] or t2[::-1] == ['M', 'A', 'S']):
                        ans += 1
    return ans

print(f"Test Solution: {solve(test_file_path)}")
print(f"Question Solution: {solve(input_file_path)}")