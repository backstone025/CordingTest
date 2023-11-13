"""
baekjoon 2566 최대값
https://www.acmicpc.net/problem/2566
"""

bowl = []
for i in range(5):
    bowl.append(list(input()))
for i in range(15):
    for j in range(5):
        if i < len(bowl[j]):
            print(bowl[j][i],end="")