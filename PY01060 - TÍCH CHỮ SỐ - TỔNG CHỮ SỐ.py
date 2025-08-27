t = int (input())
for _ in range (t):
    s =input()
    tong  = 0
    tich = 1
    for i in range (len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                tich *= int (s[i])
        else :
            tong += int (s[i])
    print (tich , tong , end =' ')
    print ()