word1 = input()
word2 = input()

prev = [0] * (len(word2) + 1)
answer = 0

for i in range(len(word1)):
    tmp = [0] * (len(word2) + 1)
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            tmp[j + 1] = prev[j] + 1
    answer = max(answer, max(tmp))
    prev = tmp[:]

print(answer)