class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        #if s%2==0:
        if not s:
            return True
        result = []
        
        for ch in s:
            if not ch.isalnum():
                #print(ch)
                continue
            # if ch in list(map(chr, range(65, 91))):
            #     result.append(ch.lower())
            # else:
            result.append(ch.lower())
        
        s = result

        start = len(s)//2 - 1

        while start >= 0 and s[start] == s[len(s) - start - 1]:
            start -= 1
        return start == -1

