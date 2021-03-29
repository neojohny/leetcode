class Solution:
    """
    @param amount: The amount you should pay.
    @return: Return the minimum number of coins for change.
    """
    def giveChange(self, amount):
        # write you code here.
        left = 1024 - amount
        total = 0
        for money in [64,16,4]:
            t,left = self.leftover(left,money)
            total += t
        
        return total + left
        
    
    def leftover(self,left,money):
        total = left//money
        left = left % money
        return total,left