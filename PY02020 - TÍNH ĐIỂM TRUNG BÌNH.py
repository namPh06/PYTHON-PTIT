n = int (input())
a = list (map (float , input().split()))
res1 , res2  = 0, 11
for x in a :
    res1  = max (res1, x)
    res2 = min (res2, x)
tong  = 0
cnt = 0
for x in a:
    if x != res1 and x != res2:
        tong += x 
        cnt += 1
print ("%.2f" % (tong / cnt))