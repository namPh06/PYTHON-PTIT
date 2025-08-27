n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
sum1, sum2 = 0, 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1 :
            sum1 += a[i][j]   
        elif i + j >  n - 1:
            sum2 += a[i][j]   
ans = abs(sum1 - sum2)
if ans <= k:
    print("YES")
else:   
    print("NO")
print(ans)
