class Solution:
    """
    @param arr: the line 
    @param k: Alex place
    @return: the time when Alex requires to buy all passes
    """
    def buyPasses(self, arr, k):
        # Write your code here.
        # counter = 0
        # while arr[k]>0:
        #     for i in range(len(arr)):
        #         if i == k and arr[k] == 1:
        #             return counter + 1
        #         if arr[i] > 0:
        #             arr[i] -= 1
        #             counter += 1
                
        #         else:
        #             continue
        counter = 0
        for i in range(len(arr)):
            if i <= k:
                # if arr[i] <= arr[k]:
                #     counter += arr[i]
                # else:
                #     counter += arr[k]
                counter += min(arr[k],arr[i])
            else:
                counter += min(arr[k]-1,arr[i])
        return counter