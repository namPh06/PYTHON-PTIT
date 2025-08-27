n = int(input())
a = list(map(int, input().split()))

cnt = [False] * (30001)

for x in a:
    cnt[x] = True   # đánh dấu số đã xuất hiện

# tìm số nhỏ nhất chưa xuất hiện
for i in range(1, n+2):   # chỉ cần duyệt đến n+1
    if not cnt[i]:
        print(i)
        break
