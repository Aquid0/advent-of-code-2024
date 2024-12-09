import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


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
    groups = []
    
    
    for i in range(n):
        if i % 2 == 0:
            diskmap += [str(id)] * int(line[i])
            groups.append((int(line[i]), str(id)))        
            id += 1
        else:
            diskmap += ["."] * int(line[i])
            groups.append((int(line[i]), "."))


    for i in range(len(groups)-1, -1, -1):
        
        file_size = groups[i][0]
        file_id = groups[i][1]
        
        if file_id != ".":
            for j in range(i):
                if groups[j][1] == "." and groups[j][0] >= file_size:
                    if groups[j][0] == file_size:
                        groups[j] = [file_size, file_id]
                        groups[i] = [file_size, "."] 
                    elif groups[j][0] > file_size:
                        groups[j:j+1] = [[file_size, file_id], [groups[j][0]-groups[i][0], "."]]
                        groups[i+1] = [file_size, "."]
                    break        
    
    
    string = ""        
    for i in groups:
        string += i[1] * i[0]
    
    
    ans = 0
    sum_id = 0
    
    
    for c, char in groups:
        for i in range(c):
            if char != ".":
                ans += sum_id * int(char)
            sum_id += 1
        
    
    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')

