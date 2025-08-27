from itertools import permutations
s = input()
v = list (s)
for x in permutations(s):
    print (''.join(x))
