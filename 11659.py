N, M = map(int, input().split())
given_number = list(map(int, input().split()))
sum = 0

for _ in range(M):
    i, j = map(int, input().split())
    for x in range(i-1, j):
        sum += given_number[x]

    print(sum)
