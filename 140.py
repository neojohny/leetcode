class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if a%b == 0:
            return 0
        answer = 1
        while n>0:
            if n%2 == 1:
                answer = (a*answer)%b
            
            a = a%b*a%b
            n = n//2
        return answer%b
