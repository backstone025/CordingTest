"""
baekjoon 18870 좌표 압축
https://www.acmicpc.net/problem/18870

딕셔너리 사용 -> 인덱스 값 접근히여 문제 해결
"""
import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

sample = sorted(list(set(X.copy())))

# dictionary comprehension
result = {sample[i]: i for i in range(len(sample))}
for i in range(N-1):
    print(result[X[i]], end=" ")
print(result[X[-1]], end="")