"""
baekjoon 2751 수 정렬하기 2
https://www.acmicpc.net/problemset?sort=ac_desc&algo=97

문제 상황: 시간 초과
퀵정렬의 시간복잡도
최선실행시간 : O(n log(n))
최악실행시간 : O(n^2)

제한 시간은 2초이지만, 최대 1,000,000개의 수를 처리한다고 하면
1000개 할 때 0.0382537841초가 걸렸으므로
11.47613523초가 걸리게 된다.
그러나 1000개 이상 수를 처리하면
RecursionError: maximum recursion depth exceeded in comparison라고 에러가 발생하는데,
이는 재귀호출 수가 많아서 발생하는 문제라고 한다.
"""
import time

# 퀵정렬 - median of three 퀵정렬
def swap(sample, i, j):
    select = sample[i]
    sample[i] = sample[j]
    sample[j] = select
    return sample

def medianOfThree(sample, left, right):
    picks = [left, int(right / 2), right]

    for i in range(3):
        test = 1
        for j in range(3):
            if i != j:
                test *= (sample[picks[j]] - sample[picks[i]])
        if test < 1:
            return picks[i]

def inPlacePartition(sample, left, right):
    if right - left < 1:
        return sample
    else:
        p = medianOfThree(sample,left,right)
        sample = swap(sample, p, right)
        i = left
        j = right - 1
        while i < j:
            while sample[i] < sample[right] and i < j:
                i += 1;
            while sample[j] > sample[right] and i < j:
                j -= 1;
            swap(sample, i, j)

        p = j
        sample = swap(sample, p, right)
        sample = inPlacePartition(sample, left, p - 1)
        sample = inPlacePartition(sample, p + 1, right)
        return sample

# 실행
start = time.time()
line = int(input())
sample = []

for i in range(1,line+1):
    sample.append(int(input()))
inPlacePartition(sample, 0, line - 1)

for i in range(0, line):
    print(sample[i])
end = time.time()
print("종료 :", end-start)