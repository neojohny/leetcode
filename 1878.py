class Solution:
    """
    @param n: length of good nums
    @return: The num of good nums of length n
    """
    def RotatedNums(self, n):
        # write your code here
        if n == 1:
            return 5
        
        if n == 2:
            return 6
            
        result = 1    
        if n%2 == 0:
            m = n/2
            while m>1:
                result = result * 7
                m -= 1
            
            return result*6
            
        else:
            m = (n-1)/2
            while m>1:
                result = result*7
                m-=1
            
            return result*5*6
        # ans =1
        # if(n==1):
        #     return 5
        # elif(n==2):
        #     return 6
        # else:
        #     if(n%2):
        #         for i in range(1,(n-1)//2):
        #             ans=ans*7
        #         ans=ans*5*6
        #         return ans
        #     else:
        #         for i in range(1,n//2):
        #             ans=ans*7
        #         ans*=6
        # return ans