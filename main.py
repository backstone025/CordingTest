"""
baekjoon 2750 수 정렬하기
https://www.acmicpc.net/problemset?sort=ac_desc&algo=97
"""
MAX = 10000

line = int(input())
sample = [MAX]

for i in range(line):
    sample.append(int(input()))

# 삽입정렬

for i in range(line):
    for j in range(i, line+1):
        if sample[i] > sample[j]:
            select = sample[i]
            sample[i] = sample[j]
            sample[j] = select

for i in range(0, line):
    print(sample[i])