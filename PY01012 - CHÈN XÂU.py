s1 = input().strip()
s2 = input().strip()
p = int (input())
tmp = s1[:p-1] + s2 + s1[p-1:]
print (tmp)