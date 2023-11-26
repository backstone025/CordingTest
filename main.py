"""
baekjoon 2667 단지번호붙이기
https://www.acmicpc.net/problem/2667

브루트 포스 -> 단지 탐색('1'인 곳 찾기){
    BFS -> 단지 개수 세기{
    }
}
"""
import sys

input = sys.stdin.readline
from collections import deque


def findNeighbor(pos, n):
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    ns = []
    for i in range(4):
        r, c = pos[0] + x[i], pos[1] + y[i]
        if (c >= 0 and c < n) and (r >= 0 and r < n):
            ns.append([r, c])
    return ns


def search(m, n):
    Visited = ([])
    result = []
    for r in range(n):
        for c in range(n):
            pos = [r, c]
            if pos not in Visited and m[pos[0]][pos[1]]:
                count = 1
                queue = deque([pos])
                Visited.append(pos)
                while queue:
                    pos = queue.popleft()
                    m[pos[0]][pos[1]] = False
                    for b in findNeighbor(pos, n):
                        if m[b[0]][b[1]]:
                            count += 1
                            queue.append(b)
                            Visited.append(b)
                            m[b[0]][b[1]] = False
                result.append(count)
            else:
                Visited.append(pos)

    return sorted(result)


N = int(input())
metrix = []
for i in range(N):
    r = [True if i == '1' else False for i in input()]
    metrix.append(r)

builds = search(metrix, N)
print(len(builds))
for i in builds:
    print(i)
