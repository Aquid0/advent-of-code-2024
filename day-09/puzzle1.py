import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def check(diskmap):
    found_dot = False
    for i in range(len(diskmap)-1):
        if diskmap[i] == ".":
            found_dot = True
        
        if found_dot and diskmap[i] != ".":
                return False
    return True
        
        
def solve(filename):
    with open(filename, 'r') as f:
        test = f.readlines()
    test = [l.strip() for l in test]
    line = "" 
    for l in test:
        line += l
    line = list(l)
    
    
    n = len(line)
    id = 0 
    diskmap = []
    
    
    for i in range(n):
        if i % 2 == 0:
            diskmap += [str(id)] * int(line[i])
            id += 1
        else:
            diskmap += ["."] * int(line[i])

    
    i = 0
    j = len(diskmap)-1
    
    
    while i <= j or not check(diskmap):
        while i <= j and diskmap[i] != ".":
            i += 1
        while j >= i and diskmap[j] == ".":
            j -= 1
        
        t = diskmap[i]
        diskmap[i] = diskmap[j]
        diskmap[j] = t 
        
    ans = 0

    for i in range(len(diskmap)):
        if diskmap[i] != ".":
            ans += i * int(diskmap[i])
    
    print(diskmap)
    
    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')