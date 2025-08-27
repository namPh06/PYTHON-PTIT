p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    n = input().strip()
    if n == '0':
        break
    k , s  = n.split()
    k = int ( k)
    res = ""
    for ch in s:
        idx = p.index(ch)
        res += p[(idx + k) % 28]
    print (res[::-1])