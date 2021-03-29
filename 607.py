class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    numbers = {}
    def add(self, number):
        # write your code here
        if number in self.numbers:
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for n in self.numbers.keys():
            if value - n in self.numbers:
                if value - n == n and self.numbers[n]>1:
                    return True
                if value - n != n: return True            
        return False