import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
res = 0
A.sort()

for k in range(N):
    find = A[k]
    i = 0  #  1번 포인터는 0번째 인덱스부터 시작
    j = N-1  #  2번 포인터는 N-1번째 인덱스부터 시작
    while i < j:
        if A[i] + A[j] == find:  #  옥죄어 오다가 두 값의 합이 find와 같다면...
            if i != k and j != k:  #  두 값 모두 찾는 값이면 안됨
                res +=1  #  하나 카운트
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:  #  두 값의 합이 찾는 값보다 작다면
            i += 1  #  1번 포인터 오른쪽으로 한 칸
        else:  #  두 값의 합이 찾는 값보다 크면
            j -= 1  #  2번 포인터 왼쪽으로 한 칸

print(res)

