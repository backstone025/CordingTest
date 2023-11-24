import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += A[j]
        if sum % M == 0:
            cnt += 1
        else:
            continue

print(cnt)