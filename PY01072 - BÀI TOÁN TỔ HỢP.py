from itertools import combinations
n, k = map(int, input().split())
nums = list(map(int, input().split()))
v = sorted(set(nums))
for comb in combinations(v, k):
    print(*comb)
