import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')

def check(object_r, object_c, igp_2, tests2, m, n):
    seen = set()
    up = True
    right = False 
    left = False 
    down = False
    tests2[object_r][object_c] = "#"
    while -1 < igp_2[0] < m and -1 < igp_2[1] < n:
        while up and -1 < igp_2[0] < m and -1 < igp_2[1] < n:
            igp_2[0] -= 1
            if igp_2[0]-1 > -1 and tests2[igp_2[0]-1][igp_2[1]] == "#":
                d = (igp_2[0]-1, igp_2[1], "U")
                if d in seen:
                    return 1                    
                else:
                    seen.add(d)
                up = False
                right = True

        while right and -1 < igp_2[0] < m and -1 < igp_2[1] < n:
            igp_2[1] += 1
            if igp_2[1]+1 < n and tests2[igp_2[0]][igp_2[1]+1] == "#":
                d = (igp_2[0], igp_2[1]+1, "R")
                if d in seen:
                    return 1
                else:
                    seen.add(d)
                right = False
                down = True 

        while down and -1 < igp_2[0] < m and -1 < igp_2[1] < n:
            igp_2[0] += 1
            if igp_2[0]+1 < m and tests2[igp_2[0]+1][igp_2[1]] == "#":
                d = (igp_2[0]+1, igp_2[1], "D")
                if d in seen:
                    return 1
                else:
                    seen.add(d)
                down = False 
                left = True

        while left and -1 < igp_2[0] < m and -1 < igp_2[1] < n:
            igp_2[1] -= 1
            if igp_2[1]-1 > -1 and tests2[igp_2[0]][igp_2[1]-1] == "#":
                d = (igp_2[0], igp_2[1]-1, "L")
                if d in seen:
                    return 1 
                else:
                    seen.add(d)
                left = False
                up = True
    return 0


def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [list(l.strip()) for l in tests]
    igp = 0
    
    m = len(tests)
    n = len(tests[0])

    for r in range(m):
        for c in range(n):
            if tests[r][c] == "^":
                igp = [r, c]
    igp_2 = igp[::]
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
                
    path = []
    for r in range(m):
        for c in range(n):
            if tests[r][c] == "1":
                path.append([r, c])

    s = set()
    path = [list(tpl) for tpl in set(tuple(lst) for lst in path)]
    print(igp_2)
    for object_r, object_c in path:     
        if object_r != igp_2[0] or object_c != igp_2[1]:
            with open(filename, 'r') as f:
                tests2 = f.readlines()
            tests2 = [list(l.strip()) for l in tests2]
            i = list(igp_2)
            if check(object_r, object_c, i, tests2, m, n) == 1:
                s.add((object_r, object_c))
    return len(s)


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}') 


# (6,3)
# (7,6)
# (7,7)
# (8,1)
# (8,3)
# (9,7)

# tried:
# 2038 too high
# 2039 
