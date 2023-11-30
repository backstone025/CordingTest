"""
baekjoon 1463 1로 만들기
https://www.acmicpc.net/problem/1463
-> 20분 소요
"""

import sys
input = sys.stdin.readline
from collections import deque

def BFS(N):
    queue = deque([[N, 0]])
    visited = {N}
    count = 0
    while queue:
        tmp = queue.popleft()
        count = tmp[1] + 1
        num = tmp[0]
        move = []
        if(num % 3 == 0 and int(num / 3) > 0):
            move.append(int(num/3))
        if(num % 2 == 0 and int(num / 2) > 0):
            move.append(int(num/2))
        if(num - 1 > 0):
            move.append(int(num-1))
        for v in move:
            if v not in visited:
                queue.append([v, count])
                visited.add(v)
            if v == 1:
                return count


N = int(input())
print(BFS(N))