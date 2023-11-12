import math

N = int(input())  # 수열의 크기
Hong_jun = list(map(int, input().split()))  # 홍준이가 제시한 자연수들
M = int(input())

def Palindrome(S, E):
    if (E - S) % 2 == 0:  # 수열이 홀수이면
        mid_idx = ((E + S) // 2) - 1
        if E == S:
            return 1
        else:
            for i in range(1, (E - S + 1) // 2 + 1):
                if Hong_jun[mid_idx - i] != Hong_jun[mid_idx + i]:
                    return 0
                else:
                    return 1


    elif (E - S) % 2 == 1:  # 수열이 짝수이면
        mid_idx = ((E + S) / 2) - 1
        for j in range(1, ((E-S+1) // 2) + 1):
            if Hong_jun[math.floor(mid_idx - j)] != Hong_jun[math.floor(mid_idx + j)]:
                return 0
            else:
                return 1

        return 1

for i in range(M):
    S, E = map(int, input().split())
    print(Palindrome(S, E))



