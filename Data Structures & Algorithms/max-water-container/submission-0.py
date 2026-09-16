class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        largest = 0
        curr = 0

        print(l)
        print(r)
        for h in heights:
            
            if n == 0: break # handles null cases
            
            while l < r:
                if heights[l] < heights[r]:
                    curr = min(heights[l],heights[r]) * (r-l)
                    largest = max(largest, curr)
                    l += 1
                elif heights[l] > heights[r]:
                    curr = min(heights[l],heights[r]) * (r-l)
                    largest = max(largest, curr)
                    r -= 1
                elif heights[l] == heights[r] and l != r:
                    curr = min(heights[l],heights[r]) * (r-l)
                    largest = max(largest, curr)
                    l += 1
        return largest

            