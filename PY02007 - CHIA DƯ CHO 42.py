import sys
a = list (map (int , sys.stdin.read().split()))
se = set ()
for x in a :
    se.add( x % 42)
print (len(se))