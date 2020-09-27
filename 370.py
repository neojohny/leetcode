
from collections import deque
class Solution:
    """
    @param expression: A string array
    @return: The Reverse Polish notation of this expression
	use stack and another list.
check for priority (and parenthis)
    """

    def convertToRPN(self, expression):
        # write your code here

        rpn = []
        stk = []
        

        for ch in expression:
            if ch == '(':
                stk.append(ch)
            elif ch == ')':
                pos = stk[::-1].index('(')
                rpn += stk[::-1][:pos]
                stk = stk[:-pos-1]
            
            elif ch[0] in '0123456789':
                rpn.append(ch)
            
            else:
                priority = self.get_prior(ch)
                while len(stk) and self.get_prior(stk[-1])>=priority:
                    rpn.append(stk.pop())
                    #rpn.append(stk[-1])
                    #stk.pop()
                stk.append(ch)
            
                
        rpn += stk[::-1]        
        return rpn
        
    def get_prior(self,s):
        if s in '()':
            return 1
        
        if s in '+-': 
            return 2
            
        if s in "*/":
            return 3
        
        return 0
    
