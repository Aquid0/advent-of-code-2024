import os

script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, "test.txt")
input_file_path = os.path.join(script_dir, "input.txt")

import re 

def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip() for l in tests]
    t = ""
    for i in tests:
        t += i
    ans = 0

    do_indices = find_indices(t, "do()")
    dont_indices = find_indices(t, "don't()")
    m = re.findall(r"mul\(\d{1,3},\d{1,3}\)", t)
    for mul in m:
        closest, source = c(do_indices, dont_indices, t.find(mul))
        if source == "do" or source == None:
            n = re.findall(r"\d{1,3},\d{1,3}", mul)[0]
            n = n.split(",")
            ans += int(n[0]) * int(n[1])
        
    return ans

def c(l1, l2, t):
    combined = [(num, "do") for num in l1] + [(num, "dont") for num in l2]
    l = [(num, source) for num, source in combined if num < t]
    if l:
        cl, s = max(l, key=lambda x:x[0]) 
        return cl, s
    return None, None

def find_indices(text, target):
    indices = []
    start = 0
    while True:
        index = text.find(target, start)
        if index == -1:  # No more occurrences
            break
        indices.append(index)
        start = index + len(target)  # Move start past this occurrence
    return indices

# print(f"Test Solution: {solve(test_file_path)}")
print(f"Question Solution: {solve(input_file_path)}")
