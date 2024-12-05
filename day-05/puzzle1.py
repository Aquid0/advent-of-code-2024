import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, "test.txt")
input_file_path = os.path.join(script_dir, "input.txt")


def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip() for l in tests]
    ans = 0 
    
    return ans
        
    

print(f"Test Solution: {solve(test_file_path)}")
print(f"Question Solution: {solve(input_file_path)}")