import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [list(l.strip()) for l in tests]
    igp = 0
    
    m = len(tests)
    n = len(tests[0])
    print(m)
    print(n)
    
    for r in range(m):
        for c in range(n):
            if tests[r][c] == "^":
                igp = [r, c]
                tests[r][c] = "1"
    
    up = True
    right = False
    left = False
    down = False

    while -1 < igp[0] < m and -1 < igp[1] < n:
        while up and igp[0] > -1:
            tests[igp[0]][igp[1]] = "1"
            igp[0] -= 1
            if igp[0]-1 > -1 and tests[igp[0]-1][igp[1]] == "#":
                up = False
                right = True
        
        while right and -1 < igp[0] < m and -1 < igp[1] < n:
            tests[igp[0]][igp[1]] = "1"
            igp[1] += 1
            if igp[1]+1 < n and tests[igp[0]][igp[1]+1] == "#":
                right = False
                down = True 
        
        while down and -1 < igp[0] < m and -1 < igp[1] < n:
            tests[igp[0]][igp[1]] = "1"
            igp[0] += 1
            if igp[0]+1 < m and tests[igp[0]+1][igp[1]] == "#":
                down = False 
                left = True
        
        while left and -1 < igp[0] < m and -1 < igp[1] < n:
            tests[igp[0]][igp[1]] = "1"
            igp[1] -= 1
            if igp[1]-1 > -1 and tests[igp[0]][igp[1]-1] == "#":
                left = False
                up = True
        
    ans = 0 
    for r in range(m):
        for c in range(n):
            if tests[r][c] == "1":
                ans += 1

    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}') 