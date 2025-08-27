while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    lst = [a, b, c, d]
    cnt = 0
    while len(set(lst)) != 1:
        new_lst = [
            abs(lst[0] - lst[1]),
            abs(lst[1] - lst[2]),
            abs(lst[2] - lst[3]),
            abs(lst[3] - lst[0])
        ]
        lst = new_lst
        cnt += 1
    
    print(cnt)
