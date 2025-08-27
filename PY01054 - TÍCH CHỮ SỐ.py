t = int (input())
for _ in range (t):
    n = input()
    tich = 1
    for x in n :
        if x != '0':
            tich *= int (x)
    print (tich)