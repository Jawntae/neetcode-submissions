class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        print(n)
        # result, pre, and post arrays
        res = [0] * n
        pre = [0] * n
        post = [0] * n
        
        #set boundaries on either side to 1
        pre[0] = post[n-1] = 1

        # iter through nums and get prefix vals
        for i in range (1,n):
            pre[i] = nums[i-1] * pre[i-1]

        #back trace through nums to get postfix vals
        for i in range(n-2, -1, -1):
            post[i] = nums[i+1] * post[i+1]

        #get result
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res
        
