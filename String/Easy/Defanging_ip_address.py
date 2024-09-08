
#Easy Problem 



class Solution(object):

    #8ms  Time
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defanged_address = ""
        for index,char in enumerate(address):
            if(char == '.'):
                defanged_address += '[.]'
            else:
                defanged_address += char
        
        return defanged_address