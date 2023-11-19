"""
baekjoon 10989 수 정렬하기 3
https://www.acmicpc.net/problem/10989

카운팅 정렬을 이용해 해결했다.
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * 10000

for i in range(N):
    num = int(input())
    nums[num-1] += 1

for i in range(10000):
    for j in range(nums[i]):
        print(i + 1)