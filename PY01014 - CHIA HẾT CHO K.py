a , k , n =  map (int , input().split())
r = a % k
if r == 0:
    start = k
else :
    start = k - r
b = []
for i in range (start , n - a + 1 , k):
    b.append(i)
if len (b) == 0 :
    print (-1)
else :
    for x in b :
        print (x , end = ' ') 