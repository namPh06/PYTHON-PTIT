t = int(input().strip())
for _ in range(t):
    s = input().strip()
    res = []
    i = 0
    n = len(s)
    while i < n:
        j = i + 1
        while j < n and s[j] == s[i]:
            j += 1
        res.append(str(j - i))
        res.append(s[i])
        i = j
    print(''.join(res))
