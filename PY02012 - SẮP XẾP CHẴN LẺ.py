n = int (input())
a = []
while len(a) < n :
    a.extend(list (map (int , input().split())))
b = []
c = []
for x in a :
    if x % 2 == 0:
        b.append(x)
    else :
        c.append(x)
b = sorted(b)
c = sorted(c , reverse= True)
idx1 , idx2 = 0 , 0
ans = []
for x in a :
    if x % 2 == 0:
        ans.append(b[idx1])
        idx1 += 1
    else :
        ans.append(c[idx2])
        idx2 += 1
print (*ans)