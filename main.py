"""
baekjoon 1697 숨박꼭질
https://www.acmicpc.net/problem/1697

방문 여부 확인할 땐 list말고 set을 쓰자.
시간 에러가 여러번 발생했는데, 원인은 전부 방문 여부 확인하는데 시간이 걸려서였다.
list[] : O(n) -> 순차적인 모든 요소 확인
set{} : O(1) -> 해시 테이블로 구현되어 있어서
"""
import sys

input = sys.stdin.readline
from collections import deque


def chaseTime(c, r):
    pos = [c, 0]
    queue = deque([pos])
    visited = {c}
    while queue:
        if pos[0] == r:
            break
        pos = queue.popleft()
        pos[1] += 1
        next = [pos[0] + 1, pos[0] * 2, pos[0] - 1]
        for n in next:
            if n >= 0 and n <= 100000 and n not in visited:
                queue.append([n, pos[1]])
                visited.add(n)
                if n == r:
                    pos = [n, pos[1]]
                    break
    return pos[1]


c, r = map(int, input().split())
print(chaseTime(c, r))
