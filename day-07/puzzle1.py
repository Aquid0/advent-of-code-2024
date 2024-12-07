import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def evaluate(string):
    t = string.replace("+", " + ").replace("*", " * ").split()
    r = int(t[0])
    
    for i in range(1, len(t), 2):
        o = t[i]
        op = int(t[i+1])
        
        if o == "+":
            r += op
        else:
            r *= op
    return r

def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip() for l in tests]
    equals = []
    nums = []
    m = {"1" : "+", "0" : "*"}
    
    for l in tests:
        t = l.split()
        equals.append(int(t[0][:len(t[0])-1]))
        nums.append(t[1:])
    
    n = len(equals)
    ans = 0

    for i in range(n):
        val = equals[i]
        tries = nums[i]
        total_combinations = 2**(len(tries)-1)
        binaries = [format(i, f'0{len(tries)}b')[1:] for i in range(total_combinations)]
        for bin_d in binaries:
            to_calc = tries[0]
            j = 1
            for b in bin_d:
                if j < len(tries)-1:
                    to_calc += m[b] + tries[j]
                else:
                    to_calc += m[b]
                j += 1
            to_calc += tries[-1]
            if evaluate(to_calc) == val:
                ans += val
                break
                
    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')

# too high 4555081945041