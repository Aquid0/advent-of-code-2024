import os
import re

script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
question_file_path = os.path.join(script_dir, 'question.txt')


def solve(filename):
    with open(filename, 'r') as f:
        line = f.read()
    stones = line.split()
    
    
    for i in range(25):
        new_stones = []
        for s in stones:    
            if s == "0":
                new_stones.append("1")
            elif len(s) % 2 == 0:
                m = len(s) // 2
                new_stones.append(s[:m])
                if all(c == "0" for c in s[m:]):
                    new_stones.append(re.sub(r'0+', '0', s[m:]))
                else:
                    new_stones.append(s[m:].lstrip('0'))
            else:
                new_stones.append(str(int(s)*2024))
        stones = new_stones
        print(len(stones))

    return len(stones)


# print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(question_file_path)}')