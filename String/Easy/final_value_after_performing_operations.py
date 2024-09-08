#Easy Problem

from functools import reduce

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return reduce(lambda x,op: x-1 if op == '--X' or op == 'X--' else x+1,  operations,0)