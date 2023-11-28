import sys
input = sys.stdin.readline

N, L = map(int, input().split())
num = list(map(int, input().split()))

num_idx = 0
D = []

for i in range(1, N+1):  #  1부터 N+1까지
    if i-L+1 >= 1:
        D.append(num[i-L : i])
    elif i-L+1 < 1:
        D.append(num[0 : i])

for i in range(len(D)):
    print(min(D[i]), end=" ")

