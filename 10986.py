import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = [0] * N
cnt = [0] * M

sum[0] = A[0]
ans = 0

for i in range(1, N):
    sum[i] = sum[i-1] + A[i]

for i in range(N):
    remind = sum[i] % M
    if remind == 0:
        ans += 1

    cnt[remind] += 1

for i in range(M):
    if cnt[i] > 1:
        ans += (cnt[i] * (cnt[i] - 1) // 2)

print(ans)

