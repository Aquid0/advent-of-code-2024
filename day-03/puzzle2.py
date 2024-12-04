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
    for i in range(len(tests)):    
        l = "do()" + tests[i] + "don't()"
        m2 = re.findall(r"do\(\)(.*?)don't\(\)", l) # List
        for i in m2: # For each do_dont
            mx = re.findall(r"mul\(\d{1,3},\d{1,3}\)", i) # find all muls inside i
            for k in mx:       
                n = re.findall(r"\d{1,3},\d{1,3}", k)[0] 
                n = n.split(",")
                ans += int(n[0]) * int(n[1])
        
        
        
                
    return ans
    

print(f"Test Solution: {solve(test_file_path)}")
# print(f"Question Solution: {solve(input_file_path)}")
