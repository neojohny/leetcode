class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # Write your code here
        if n == 1:
            return True
        com = 2
        while com <n:
            com = com * 2
            #print(com)
        
        return com == n