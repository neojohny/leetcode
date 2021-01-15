class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    def luckyNumber(self, n):
        # Write your code here
        result = 0
        if not n:
            return result
        for i in range(n):
            if '8' in str(i):
                result += 1
        return result 
