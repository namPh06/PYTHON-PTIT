while True:
    n = int (input())
    if n == 0 :
        break
    a = []
    for i in range (n):
        a.append(int(input()))
    a.sort()
    if a[0] != a[-1]:
        print (a[0] , a[-1])
    else :
        print ("BANG NHAU")
    