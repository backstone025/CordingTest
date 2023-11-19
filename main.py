"""
baekjoon 10989 수 정렬하기 3 (error)
https://www.acmicpc.net/problem/10989

이번 시도는 병합정렬을 이용하는 방법을 사용했다.
많은 수의 재귀호출은 불가능하기에 반복문을 이용한 시도다.
완전하지 않고, 여러번 시도했으나 실패했고, 다른 대안을 찾았기에 이 방법은 포기한다.
"""

# N = int(input())
nums = []


def mergeSort(nums):
    s = 0
    e = len(nums)-1
    m = int(e / 2)
    str = [[-1,len(nums),True]]
    while True:
        while e - s > 1 and str[-1][2]:
            str.append([s, e, True])
            e = m
            m = int((e-s) / 2) + s

        l = s
        r = m + 1
        box = nums.copy()
        for i in range(s, e+1):
            if (box[l] < box[r] and l <= m) or r > e:
                nums[i] = box[l]
                l+=1
            else:
                nums[i] = box[r]
                r+=1
        s = e+1
        e = str[-1][1]
        if not str[-1][2]:
            str.pop()
            e = str[-1][1]
            m = int((e - s) / 2) + s
        if s == e or s == len(nums):
            s = str[-1][0]
            e = str[-1][1]
            m = int((e-s) / 2) + s
            str[-1][2] = False
        if len(str)<2:
            break


import random

# for i in range(3):
#    nums.append(random.randint(1, 100))
nums.append(8)
nums.append(6)
nums.append(3)
#nums.append(5)
nums.append(10)

print(nums)
mergeSort(nums)
print(nums)
