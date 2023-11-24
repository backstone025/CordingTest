"""
baekjoon 1260 DFS와 BFS
https://www.acmicpc.net/problem/1260

반복문을 활용한 BFS를 사용했다.
규모가 작고 최단 경로 찾을 땐 BFS를 사용해야 한다.
"""
import sys

input = sys.stdin.readline
from collections import deque


def findNeighbor(n, m, pos):
    r = [1, 0, -1, 0]
    c = [0, 1, 0, -1]
    ns = []
    for i in range(4):
        x = pos[1] + c[i]
        y = pos[0] + r[i]
        if 0 <= x <= m and 0 <= y <= n:
            ns.append([y, x])
    return ns


def search(matrix, n, m):
    pos = [0, 0, 1]
    queue = deque([pos])
    visited = [[0, 0]]
    while queue:
        pos = queue.popleft()
        ns = findNeighbor(n, m, pos)
        for v in ns:
            if matrix[v[0]][v[1]] and (v not in visited):
                visited.append(v.copy())
                v.extend([pos[2] + 1])
                if v[0] == n and v[1] == m:
                    return v[2]
                queue.append(v)
    return -1


N, M = map(int, input().split())
matrix = []
for i in range(N):
    line = [True if n == '1' else False for n in input()]
    matrix.append(line)

print(search(matrix, N - 1, M - 1))
