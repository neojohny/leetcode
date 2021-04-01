class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates:
          return []
        candidates.sort()
        result = []
        self.dfs(candidates,target,[],result,0)
        return result
        

    def dfs(self, can, target,sub,results,index):
      #print(can)
      if target==0:
        sub.sort()
        if sub not in results:
          results.append(list(sub))
        return
      if target < 0:
        return

      for i in range(index,len(can)):
        # if can[i] + sum(sub) <= target:
        #   #break
          #print('sub ',sub)
          sub.append(can[i])
          self.dfs(can,target-can[i],sub,results,i)
          sub.pop()