"""
baekjoon 11724 연결 요소의 개수
https://www.acmicpc.net/problem/11724

맨 처음 값을 넣어줄 경우를 따지지 않아 문제가 발생했다.
맨 처음 queue값 넣을 때 node의 개수가 충분한지(pop()에러 방지)
만약 그렇다면 넣는 동시에 nodes에서 빼주기
"""

import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
nodes = {i for i in range(1, N+1)}
edges = {i : [] for i in range(1, N+1)}
for i in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

queue = deque([])
if len(nodes) >= 1:
    queue.append(nodes.pop())
count = 1
while nodes:
    n = queue.popleft()
    for k in edges[n]:
        if k in nodes:
            nodes.remove(k)
            queue.append(k)
    if len(queue) == 0:
        count += 1
        queue.append(nodes.pop())
print(count)