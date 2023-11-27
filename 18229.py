N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
sum_array = [0] * N

for i in range(M):
    for j in range(N):
        sum_array[j] += arr[j][i]
        if sum_array[j] >= K:
            print(j + 1, i + 1)
            exit()

