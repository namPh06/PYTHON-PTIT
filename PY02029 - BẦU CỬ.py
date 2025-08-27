n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (m + 1)
for x in a:
    cnt[x] += 1
tmp = []
for i in range(1, m + 1):
    if cnt[i] > 0:
        tmp.append(cnt[i])
res = sorted(list(set(tmp)), reverse=True)
if len(res) < 2:
    print("NONE")
else:
    idx = res[1]
    stt = -1
    for i in range(1, m + 1):
        if cnt[i] == idx:
            stt = i
            break

    print(stt)