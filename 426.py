class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        result = []
        path = []
        self.dfs(s,path,result)
        return result

    def dfs(self,s,path,result):
        #if not s or len(path)>4:

        if len(path)==4:
            if not s:
                result.append('.'.join(path))
            return
        
        for i in range(1,4):
            # if s[0]==0  and i>1:
            #     break
            if i <= len(s):
                if s[0]=='0' and i>1:
                    break

                if int(s[:i])<=255:
                    path.append(s[:i])
                    self.dfs(s[i:],path,result)
                    path.pop()
                


            # if i <= len(s):            
            #     currentnum = s[:i]
            #     if int(currentnum)<=255:
            #         path.append(currentnum)
            #         self.dfs(s[i:],path,result)
            #         path.pop()
            #     if s[0] == '0':
            #         break            
        
    # def restoreIpAddresses(self, s):
    #     # write your code here
    #     path = []
    #     result = []
    #     self.dfs(s,path,result)
    #     return result
        
    
    # def dfs(self,s,path,result):
    #     #print(len(path))
    #     if len(path)==4:
    #         if not s:
    #             result.append('.'.join(path))
    #         return
        
    #     for i in range(1,4):
    #         if i <= len(s):            
    #             currentnum = s[:i]
    #             if int(currentnum)<=255:
    #                 path.append(currentnum)
    #                 self.dfs(s[i:],path,result)
    #                 path.pop()
    #             if s[0] == '0':
    #                 break