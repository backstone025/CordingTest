"""
baekjoon 2563 색종이
https://www.acmicpc.net/problem/2563
"""

paper = []
for i in range(100):
    l = []
    for j in range(100):
        l.append(0)
    paper.append(l)

def setMetrix(value, row, col):
    for i in range(row, row + 10):
        for j in range(col, col + 10):
            paper[i][j] = value

num = int(input())
for i in range(num):
    row, col = map(int, input().split())
    setMetrix(1, row, col)

s = 0
for i in range(100):
    for j in range(100):
        s += paper[i][j]
print(s)