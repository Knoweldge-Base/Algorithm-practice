#Easy
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        found = []
        for index,curr_str in enumerate(words):
            if x in curr_str:
                found.append(index)
        return found
        