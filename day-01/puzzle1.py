import os

script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, "test.txt")
input_file_path = os.path.join(script_dir, "input.txt")


def solve(filename):
    with open(filename, 'r') as f:
        tests = f.readlines()
    tests = [l.strip() for l in tests]
    v1 = []
    v2 = []
    for l in tests:
        v1.append(int(l.split()[0]))
        v2.append(int(l.split()[1]))

    v1.sort()
    v2.sort()

    s = 0

    for i in range(len(v1)):
        s += abs(v1[i]-v2[i])
    return s


print(f"Test Solution: {solve(test_file_path)}")
# print(f"Question Solution: {solve(input_file_path)}")
