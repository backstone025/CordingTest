"""
baekjoon 1181 단어 정렬
https://www.acmicpc.net/problem/1181
"""
import sys
input = sys.stdin.readline

def separate(s):
    if(s.isdigit()):
        return int(s)
    else:
        return s

N = int(input())
member = []
for i in range(N):
    o,n = map(separate, input().split())
    member.append([o,i,n])

member.sort()
for i in range(N):
    print(member[i][0],member[i][2])