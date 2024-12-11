import os


script_dir = os.path.dirname(__file__)
test_file_path = os.path.join(script_dir, 'test.txt')
question_file_path = os.path.join(script_dir, 'question.txt')


def solve(filename):
    with open(filename, 'r') as f:
        line = f.read()
    stones = line.split()
    dp = {}
    
    def calc(s, n): 
        key = f"{s},{n}"
        if key in dp:
            return dp[key]
        
        if n == 0:
            return 1
        else:
            total = 0 
            if (s == "0"):
                total = calc("1", n-1)
            elif len(s) % 2 == 0: 
                m = len(s) // 2
                l = s[:m]
                r = ""
                if all(c == "0" for c in s[m:]):
                    r = "0"
                else:
                    r = s[m:].lstrip("0")
                total = calc(l, n-1) + calc(r, n-1)
            else:
                total = calc(str(int(s)*2024), n-1)
            dp[key] = total
            return total

    ans = 0 
    print(stones)
    for st in stones:
        ans += calc(st, 75)

    return ans


print(f'Test Solution: {solve(test_file_path)}')
print(f'Question Solution: {solve(question_file_path)}')