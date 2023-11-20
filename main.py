"""
baekjoon 1427 소트인사이드
https://www.acmicpc.net/problem/1427
"""
import sys
input = sys.stdin.readline

N = int(input())
Nlen = len(str(N))
for i in range(9,-1,-1):
    num = N
    count = 1
    while num != 0:
        pn = num%10
        num = int(num/10)
        if pn == i:
            print(pn,end="")
            tmp = int(N / (10**count))
            N %= 10**(count-1)
            N = N + tmp * (10**(count-1))
            count -= 1
            Nlen -= 1
        count += 1;
for i in range(Nlen):
    print(0,end="")