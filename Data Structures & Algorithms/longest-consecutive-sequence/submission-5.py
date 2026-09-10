class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        
        curr = nums[0]
        streak = 0
        res = 0
        i = 0

        while i < len(nums):

            #if curr is not a consecutive #, reset streak and
            # start new consecutive streak with curr idx
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
                
            while i < len(nums) and nums[i] == curr:
                i += 1

                #increase streak  since consecutive is found 
            streak += 1
            curr += 1
            res = max(res, streak)
        return res