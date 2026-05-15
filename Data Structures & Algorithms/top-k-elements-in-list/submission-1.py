class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        #populates dict
        for num in nums:
            count[num] = count.get(num,0) + 1

        # adds and sorts key-value pairs to arr[]
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        # for < k elements, append keys to result[]
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
