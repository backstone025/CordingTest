import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

target_index = A.index(-1)
left_min = min(A[:target_index])
right_min = min(A[target_index+1:])

print(left_min + right_min)










