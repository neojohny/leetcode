class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        answer = 1
        if n < 0:
            x = 1/x
            n = -n
        tmp = x
        while n>0:
            #answer = answer * answer
            if n%2 == 1:
                answer = answer * tmp
            tmp = tmp * tmp
            n = n//2
            
        return answer
    