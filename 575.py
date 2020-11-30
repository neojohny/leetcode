class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        #result = ''
        if not s:
            return ''
        pos,result = self.helper(0,s)
        return result
                
            
        
    def helper(self,i,s):
        result = ''
        while i<len(s):
            if s[i] not in '0123456789' and s[i] not in ['[',']']:
                result += s[i]
                
            elif s[i] == ']':
                return i,result
            
            else:
                num = "0"
                
                while i< len(s) and s[i] in '0123456789':
                    num += s[i]
                    i += 1
                    #print(int(num))

                i,r = self.helper(i+1,s)
                result += int(num)*r
            
            i += 1
        return i,result
                