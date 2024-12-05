import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip() for l in tests]
    i = 0
    
    ordering = {} # BEFORE | ALL AFTERS
    
     
    while i < len(tests) and (tests[i] != "\n" and tests[i] != ""):
        l = tests[i]
        l = l.split('|')
        
        if l[0] not in ordering:
            ordering[l[0]] = [l[1]]
        else:
            ordering[l[0]].append(l[1])    
        i += 1
    i += 1
    updates = []
    while i < len(tests): 
        j = tests[i].split(",")
        updates.append(j)
        i += 1
    
    v = []
    
    for u in updates:
        incorrect = False
        seen = []
        for num in u:
            if num in ordering and set(seen) & set(ordering[num]):
                incorrect = True
            seen.append(num)  
        if incorrect:   
            new_ordering = []
            for num in u:
                if num in ordering:
                    new_ordering.append([num, set(seen) & set(ordering[num])])
                else:
                    new_ordering.append([num, []])
            new_ordering.sort(reverse=True, key=lambda x: len(x[1]))
            v.append([x[0] for x in new_ordering])

    ans = 0
    for u in v:
        m = len(u)//2
        ans += int(u[m])
    
    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')

