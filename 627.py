class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        dic = {}
        for ch in s:
            if ch in dic:
                del(dic[ch])
            else:
                dic[ch] = ch
        
        if len(dic) >0 :
            return len(s) - len(dic) + 1
        
        return len(s)
