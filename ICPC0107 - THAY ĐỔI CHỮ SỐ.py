import sys
data = sys.stdin.read().strip().split()
t = int(data[0])
idx = 1
for _ in range(t):
    p, q = data[idx], data[idx+1]
    idx += 2
    x1 = data[idx]; idx += 1
    x2 = data[idx]; idx += 1
    s1 = x1.replace(p, q)
    s2 = x1.replace(q, p)
    res1 = min(int(s1), int(s2))
    res2 = max(int(s1), int(s2))
    s3 = x2.replace(p, q)
    s4 = x2.replace(q, p)
    res3 = min(int(s3), int(s4))
    res4 = max(int(s3), int(s4))
    print(res1 + res3, res2 + res4)
