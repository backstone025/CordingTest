word1 = input()
word2 = input()

word1_substrings = set([word1[i:j+1] for i in range(len(word1)) for j in range(i, len(word1))])
word2_substrings = set([word2[i:j+1] for i in range(len(word2)) for j in range(i, len(word2))])

common_substring = []
for i in range(len(word1_substrings)):
    for j in range(len(word2_substrings)):
        if list(word1_substrings)[i] == list(word2_substrings)[j]:
            common_substring.append(list(word2_substrings)[j])
        else:
            continue

if len(common_substring) != 0:
    max_str = common_substring[0]
    for i in range(1, len(common_substring)):
        if len(max_str) < len(common_substring[i]):
            max_str = common_substring[i]
    print(len(max_str))

else:
    print("0")

