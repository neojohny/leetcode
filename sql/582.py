class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        dic = {}
        return self.dfs(s,0,wordDict,dic)

    
    def dfs(self,s,index,wordDict,dic):
        if s[index:] in dic:
            return dic[s[index:]]
        if index == len(s):
            return [""]
        parts = []
        for i in range(index+1,len(s)+1):
            sub = s[index:i]
            if sub not in wordDict:
                continue
            latersubs = self.dfs(s,i,wordDict,dic)
            print(latersubs)

            for item in latersubs:
                if item:
                    parts.append(sub + ' ' + item)
                else:
                    parts.append(sub)        
            
        dic[s[index:]] = parts
        return parts
