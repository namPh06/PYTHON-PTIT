t = int (input())
for _ in range (t):
    s = input()
    cnt = 0
    tong  = 0
    cnt1  = 0
    for i in range (len(s)):
        if i %  2 == 0:
            tong += int (s[i])
        else :
            cnt1 += 1
            if s[i] == '0' :
                cnt += 1
    if cnt1 == cnt :
        print (tong , 0 , end = ' ')
    else :
        tich = 1
        for i in range (len(s)):
            if i % 2 != 0:
                if s[i] != '0':
                    tich *= int (s[i])
        print (tong , tich , end = ' ')
    print ()

