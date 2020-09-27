class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        # unique_chars = set([])
        # j = 0
        # n = len(s)
        # longest = 0
        # for i in range(n):
        #     while j < n and s[j] not in unique_chars:
        #         unique_chars.add(s[j])
        #         j += 1
        #     longest = max(longest, j - i)
        #     print(unique_chars,s[i])
        #     unique_chars.remove(s[i])

        # return longest
        
        
        # n = len(s)
        # seen = set([])
        # length = 0
        # j=0
        # for i in range(n):
        #     while j<n and s[j] not in seen:
        #         seen.add(s[j])
        #         j += 1

        #         length = max(length,j-i)
        #     seen.remove(s[i])
            
        # return length
        
        start = 0
        n = 0#len(s)
        seen = set([])
        length = 0
        for ch in s:
            while ch in seen:
                seen.remove(s[start])
                start += 1
                n -= 1
            
            n+=1
            seen.add(ch)
            length = max(length,n)
            
        return length
        
        # if s == '':

        #     return 0

        # window = set()

        # left = 0 

        # max_len = 0

        # cur_len = 0

        

        # for ch in s:

        #     # 从前向后删除，直到删除了ch

        #     while ch in window:

        #         window.remove(s[left])

        #         left += 1

        #         cur_len -= 1

        #     # 添加ch

        #     window.add(ch)

        #     cur_len += 1

        #     # 更新长度

        #     max_len = max(max_len, cur_len)

        # return max_len