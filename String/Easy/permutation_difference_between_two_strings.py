#Easy

class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        x = 0
        for index,char in enumerate(s):
            x += abs(index - t.index(char))
        return x