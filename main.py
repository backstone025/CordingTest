"""
baekjoon 2566 최대값
https://www.acmicpc.net/problem/2566
"""
max = 0
col, row = 1,1

for i in range(9):
    list = input().split()
    for j in range(9):
        if (max < int(list[j])):
            max = int(list[j])
            col = i + 1
            row = j + 1
print(max)
print(col,row)