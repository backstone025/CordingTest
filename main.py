"""
baekjoon 1260 DFS와 BFS
https://www.acmicpc.net/problem/1260

list comprehension을 사용하여 코드를 줄이고자 했다.
"""
import sys
from collections import Counter

input = sys.stdin.readline

def BFS(n, s, ns):
    stack = [s]
    record = [s]
    check_n = {i:True for i in range(1,n+1)}
    check_n[s] = False
    while stack:
        n_pos = stack.pop(0)
        e_list = ns[n_pos]
        for j in range(len(e_list)):
            if check_n[e_list[j]]:
                stack.append(e_list[j])
                record.append(e_list[j])
                check_n[e_list[j]] = False
        if Counter(check_n.values())[False] == n:
            break
    return record

def DFS(n, s, ns):
    n_pos = s
    record = [s]
    stack = [s]
    check_n = {i:True for i in range(1,n+1)}
    check_n[s] = False
    while True:
        e_list = ns[n_pos]
        for j in range(len(e_list)):
            if check_n[e_list[j]]:
                stack.append(e_list[j])
                record.append(e_list[j])
                check_n[e_list[j]] = False
                n_pos = e_list[j]
                break
        else:
            stack.pop()
            if len(stack) == 0:
                break
            n_pos = stack[-1]
            continue
        if Counter(check_n.values())[False] == n:
            break
    return record

node, edge, start = map(int, input().split())
nodes = {i:[] for i in range(1, node+1)}
for i in range(edge):
    a, b = list(map(int, input().split()))
    nodes[a].append(b)
    nodes[b].append(a)
for k, v in nodes.items():
    nodes[k] = sorted(v)

DFS_list = DFS(node, start, nodes)
for v in range(len(DFS_list)-1):
    print(DFS_list[v], end=" ")
print(DFS_list[-1])
BFS_list = BFS(node, start, nodes)
for v in range(len(BFS_list)-1):
    print(BFS_list[v], end=" ")
print(BFS_list[-1])