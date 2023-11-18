"""
baekjoon 25305 커트라인
https://www.acmicpc.net/problem/25305
"""

N, k = map(int, input().split())
x = list(map(int, input().split()))
winner = []
for i in range(k):
    winner.append(x[i])
for i in range(k,N):
    tmp = x[i]
    for j in range(k):
        if(tmp > winner[j]):
            candidate = winner[j]
            winner[j] = tmp
            tmp = candidate
result = winner[0]
for i in range(1, k):
    if(result>winner[i]):
        result = winner[i]
print(result)