from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        word_list = re.split(r'[,.?!\s]+', paragraph)
        filtered_word_list = [word.lower() for word in word_list if word.lower() not in set(banned)]
        result_sentence = ' '.join(filtered_word_list)
        final_word = re.findall(r'\w+', result_sentence)
        counter = Counter(final_word)

        return counter.most_common(1)[0][0]


a = Solution()
a.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"])