s1 = input().lower()
s2 = input().lower()
se1 = set (s1.split())
se2 = set (s2.split())
hop = se1 & se2
a = sorted (list(hop))
tmp = se1 | se2
b = sorted (list(tmp))
for x in  b:
    print (x, end = ' ')
print ()
for x in a :
    print (x, end = ' ')
