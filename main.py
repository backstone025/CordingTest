"""
baekjoon 2738 항렬 덧셈
https://www.acmicpc.net/problem/2738
"""

column, row = map(int, input().split())
A = []
B = []

for i in range(column):
    input_list = input().split()
    l = []
    for j in range(row):
        l.append(int(input_list[j]))
    A.append(l)
for i in range(column):
    input_list = input().split()
    l = []
    for j in range(row):
        l.append(int(input_list[j]))
    B.append(l)
for i in range(column):
    for j in range(row):
        if(j != row - 1):
            print(A[i][j] + B[i][j], end=" ")
        else:
            print(A[i][j] + B[i][j])