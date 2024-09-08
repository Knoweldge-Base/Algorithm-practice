#easy

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        x=0
        for index,char in enumerate(stones):
            x += 1 if char in jewels else 0
        return x