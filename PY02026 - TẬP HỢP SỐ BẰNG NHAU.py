n , m = map (int , input().split())
a = list (map (int , input().split()))
b = list (map (int , input().split()))
A = set (a)
B = set (b)
A1 = sorted(list (A))
B1 = sorted(list (B))
# for x in A1:
#     print (x, end = ' ')
# print()
# for x in B1:
#     print (x, end = ' ')
if A1 == B1 :
    print ("YES")
else :
    print ("NO")