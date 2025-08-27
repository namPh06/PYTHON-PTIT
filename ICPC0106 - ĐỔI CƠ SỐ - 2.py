def solve(n):  
    if n == 0:
        return "0"
    a = []
    while n > 0:
        a.append(str(n % 4))
        n //= 4
    return ''.join(reversed(a))

t = int(input())
for _ in range(t):
    b = int(input())
    s = input().strip()
    tmp = int(s, 2) 
    
    if b == 2:
        print(s)
    elif b == 4:
        print(solve(tmp))
    elif b == 8:
        print(oct(tmp)[2:])
    else:
        print(hex(tmp)[2:].upper())