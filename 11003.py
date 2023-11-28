import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
num = list(map(int, input().split()))
D  = deque()

for i in range(N):
    while D and D[-1][0] > num[i]:
        D.pop()
    D.append((num[i], i))
    if D[0][1] <= i - L:
        D.popleft()
    print(D[0][0], end=" ")
