class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        f = 0
        b = len(numbers) -1

        while f < b:
            curr = numbers[f] + numbers[b]
            
            # if greater that target, reduce larger side
            if curr > target:
                b -= 1

            # if smaller than target, increase smaller side
            elif curr < target:
                f += 1

            else: return [f + 1, b + 1]

        return []