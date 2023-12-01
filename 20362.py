import sys
from collections import defaultdict
input = sys.stdin.readline

N, S = input().split()  #  채팅 개수, 정답자 닉네임
count = 0  #  아쉬운 사람 수
d = defaultdict(list)  #  딕셔너리 초기화

for i in range(int(N)):
    A, B = input().split()
    d[A] = B  #  "A 닉네임 : B 답안" 형식으로 딕셔너리 요소 추가

ans = d[S]  #  정답 저장
for i in d.keys():  #  i는 딕셔너리의 key들
    if d[i] != ans:  #  답이 틀리면
        continue  #  그냥 건너뛰고

    elif i != S:  #  만약 닉네임이 S가 아닐 경우
        count += 1  #  억울한 사람 추가

    elif i == S:  #  key가 원래 정답자인 경우
        break

print(count)

