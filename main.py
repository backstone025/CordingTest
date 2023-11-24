"""
baekjoon 2606 바이러스
https://www.acmicpc.net/problem/2606

연습할 겸 DFS를 이용해 구현했다.
"""
import sys
input = sys.stdin.readline
from collections import deque

def DFS(es):
    visited = [1]
    stack = [None, 1]
    pos = 1
    while stack and not pos is None:
        for end in es[pos]:
            if end not in visited:
                es[pos].popleft()
                visited.append(end)
                stack.append(end)
                pos = end
                break
        else:
            stack.pop()
            pos = stack[-1]
    return len(visited)-1


n_num = int(input())
e_num = int(input())

inputs = []
for _ in range(e_num):
    h, t = map(int, input().split())
    inputs.append((h, t))
    inputs.append((t, h))
inputs.sort()
edges = {i+1 : deque([]) for i in range(n_num)}
for t in inputs:
    edges[t[0]].append(t[1])

print(DFS(edges))