import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def group(l):
    res = []
    c = 1 
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            c += 1
        else:
            res.append((c, l[i-1]))
            c = 1 
    res.append((c, l[-1]))
    return res


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
    
    
    groups = group(diskmap)
    ans = 0
        
    # Check for if the group has already been swapped with True/False
    for i in range(len(groups)-1, -1, -1):
        if groups[i][1] != ".":
            for j in range(i):
                if groups[j][1] == "." and groups[j][0] >= groups[i][0]:
                    if groups[j][0] == groups[i][0]: # i is the number group, j is the dot group
                        groups[j] = (groups[i][0], groups[i][1])
                        groups[i] = (groups[i][0], ".")
                    elif groups[j][0] > groups[i][0]:
                        temp_c = groups[i][0]
                        groups[j:j+1] = [(groups[i][0], groups[i][1]), (groups[j][0]-groups[i][0], ".")]
                        groups[i+1] = (temp_c, ".")
                    break        


    string = ""        
    for i in groups:
        string += i[1] * i[0]

    for i in range(len(string)):
        if string[i] != ".":
            ans += i * int(string[i])
    
    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')

# too low 86209592143
# too low 86209591055
#         59426879847
# not right 86426172942
