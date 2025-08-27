tmp = "ABC"
def solve(s, length):
    if len(s) == length:
        if 'A' in s and 'B' in s and 'C' in s:
            cntA = s.count('A')
            cntB = s.count('B')
            cntC = s.count('C')
            if cntA <= cntB <= cntC:
                print(s)
        return 
    for ch in tmp:
        solve(s + ch, length)
n = int(input())
for x in range(3, n + 1):
    solve("", x)
