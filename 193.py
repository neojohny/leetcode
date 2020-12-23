from collections import deque
class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        # write your code here
    #     if not s:
    #         return 0
    #     longest = 0
    #     for i in range(len(s)):
    #         length = self.findlength(s,i,i+1)
    #         longest = max(longest,length)
            
    #     return longest
        
        
    # def findlength(self,string,start,end):
    #     while start >0 and end < len(string):

    #         if string[start]!=string[end]:
    #             break
    
    #         start -= 1
    #         end += 1
    #     return end - start + 1
        st = [-1]
        longest = 0
        for i in range(len(s)):
            c = s[i]
            if c == ')':
                st.pop()
                if not st:
                    st.append(i)
                else:    
                    longest = max(longest,i-st[-1])
            else:
                st.append(i)
        return longest