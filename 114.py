class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        print(self.mi(m+n-2),self.mi(min(m,n)-1),self.mi(m+n-1-min(m,n)))
        print(self.mi(m+n-2)/self.mi(min(m,n)-1)/self.mi(m+n-1-min(m,n)))
        return int(round(self.mi(m+n-2)/self.mi(min(m,n)-1)/self.mi(m+n-1-min(m,n)),0))
    
    def mi(self,x):
        result = 1
        while x>0:
            result = result * x
            x -= 1
        return result
            
            
    