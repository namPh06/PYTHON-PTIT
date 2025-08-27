from itertools import combinations
n , k = map (int , input().split())
a = input().split()
se = sorted(set(a))
for x in  combinations(se,k):
    print (' '.join(x))