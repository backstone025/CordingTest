N, X, K = map(int, input().split())

li = [0] * N  #  컵 세팅하기
li[X-1] = 1  #  X번 컵에 공 넣은 것을 1로 표시

for i in range(K):
    A, B = map(int, input().split())
    li[A-1], li[B-1] = li[B-1], li[A-1]  #  컵 스왑

res_idx = li.index(1)  #  공 들어 있는 인덱스 반환
print(res_idx + 1)
