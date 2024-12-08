import os
from itertools import product

script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
input_file_path = os.path.join(script_dir, 'input.txt')


def evaluate(string, val):
    t = string.split()
    r = int(t[0])

    for i in range(1, len(t), 2):
        o = t[i]
        op = int(t[i+1])

        if o == "+":
            r += op
        elif o == "*":
            r *= op
        else:
            x = str(r) + str(op)
            r = int(x)
        
        if r > val:
            return -1

    return r


def generate(tries):
    slots = len(tries)-1
    all_expressions = []
    combinations = list(product(["+", "*", "||"], repeat=slots))

    for comb in combinations:
        expr = tries[0]
        for j in range(len(comb)):
            expr += f" {comb[j]} {tries[j+1]}"
        all_expressions.append(expr)
    return all_expressions


def solve(filename):    
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip() for l in tests]
    equals = []
    nums = []
    m = {"1": "+", "0": "*"}   

    for l in tests:
        t = l.split()
        equals.append(int(t[0][:len(t[0])-1]))
        nums.append(t[1:])

    n = len(equals)
    ans = 0

    for i in range(n):
        val = equals[i]
        tries = nums[i]
        all_expressions = generate(tries)
        for expr in all_expressions:
            if evaluate(expr, val) == val:
                ans += val
                break

    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(input_file_path)}')

# too high 4555081945041
