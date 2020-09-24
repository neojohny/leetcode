class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        result = []
        path = []
       #self.memo = {}
        self.dfs(s,path,result,wordDict)
        
        return result
            
    
    def dfs(self,s,path,result,wordDict):
        # if s in self.memo:
        #     result.append(str(' '.join(path+self.memo[s])))
        #     return 
        
        if len(s)==0:
            result.append(str(' '.join(path)))
            return
        
        
        for i in range(1,len(s)+1):

            if s[:i] in wordDict:
                path.append(s[:i])
                #print(path)
                
                self.dfs(s[i:],path,result,wordDict)
                path.pop()
        #self.memo[s] = path        
                
    # def wordBreak(self, s, wordDict):
    #     return self.dfs(s, wordDict, {})
    
    # # 找到 s 的所有切割方案并 return
    # def dfs(self, s, wordDict, memo):
    #     if s in memo:
    #         return memo[s]
            
    #     if len(s) == 0:
    #         return []
            
    #     partitions = []
        
    #     for i in range(1, len(s)):
    #         prefix = s[:i]
    #         if prefix not in wordDict:
    #             continue
    #         print(prefix)
    #         sub_partitions = self.dfs(s[i:], wordDict, memo)
    #         for partition in sub_partitions:
    #             partitions.append(prefix + " " + partition)
                
    #     if s in wordDict:
    #         partitions.append(s)
            
    #     memo[s] = partitions
    #     return partitions