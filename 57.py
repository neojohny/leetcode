class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        results = []
        if not numbers:
          return []
        for i in range(len(numbers)):
          start = 0
          end = len(numbers)-1
          target = -numbers[i]
          
          while start < end:
            
            if start == i or end==i:
              start+=1
              continue
                
            current = numbers[start] + numbers[end]
            if current == target:
              result = [numbers[start],numbers[end],numbers[i]]
              #print()
              print(result)
              result.sort()
              if result not in results:
                #continue
                  results.append(result)
              start += 1
              
            if current < target:
              start += 1
            if current > target:
              end -= 1
        return results
    