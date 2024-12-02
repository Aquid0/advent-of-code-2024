import os

script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, "test.txt")
input_file_path = os.path.join(script_dir, "input.txt")


def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip().split() for l in tests]
    c = 0
    for rep in tests:
        rep = [int(l) for l in rep]
        if check_increase(rep) or check_decrease(rep):
            c+=1
    return c
    
    
def check_increase(report):
    for i in range(len(report)-1):
        if not (report[i] < report[i+1] and 1 <= report[i+1]-report[i] <= 3):
            return False
    return True

def check_decrease(report):
    for i in range(len(report)-1):
        if not (report[i] > report[i+1] and 1 <= report[i]-report[i+1] <= 3):
            return False
    return True

print(f"Test Solution: {solve(test_file_path)}")
print(f"Question Solution: {solve(input_file_path)}")
