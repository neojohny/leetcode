class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if s is None:
            return None
        aa = [0,0]
        result = ''
        for i in range(len(s)):
            #print(i)
            odd = self.helper(s,i,i)
            even = self.helper(s,i,i+1)
            #print(odd,even)
            if len(odd)>len(result):
                result = odd
            if len(even)>len(result):
                result = even

        return result

    def helper(self, s,left,right):
        while left >= 0 and right <=len(s)-1 and s[left]==s[right]:
            left -= 1
            right +=1
        
        return s[left+1:right]
