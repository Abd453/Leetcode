class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split(' ')
        index_list = [None] * len(word_list)

        for word in word_list:
            index_list[int(word[-1])-1] = word[:-1]

        return " ".join(index_list)