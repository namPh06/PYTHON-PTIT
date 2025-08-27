n = int (input())
a = list (map (int, input().split()))
res = 10**9
id = 0
for i in range (n):
    tong = 0
    for j in range (n):
        if a[i] > a[j]:
            tong += (a[i] - a[j])
        else :
            tong += (a[j] - a[i])
    if tong < res:
        res =  tong 
        id = i 
print (res , a[id] )