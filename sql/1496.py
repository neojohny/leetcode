class Solution(SolBase):
    def rand10(self):
        result = 0
        for _ in range(10):
            result += self.rand7()
        return result%10
        first =41
        while first > 40:
            first = self.rand7()*self.rand7()
        
        return first