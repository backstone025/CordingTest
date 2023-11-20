"""
baekjoon 1181 단어 정렬
https://www.acmicpc.net/problem/1181
"""
import sys
input = sys.stdin.readline

N = int(input())
words = [[-1,'null']]
for i in range(N):
    w = input()
    words.append([len(w), w])
words.sort()

for i in range(1, N+1):
    if words[i][1] != words[i-1][1]:
        print(words[i][1], end="")