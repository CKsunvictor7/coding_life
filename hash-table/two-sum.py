class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # best solution wih 52m
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [i, seen[remaining]]
            seen[v] = i  # to make later nums check previous numbers quickly
        return []

        """
        # more simple but slower(840m)
        for i in range(len(nums)):
            try:
                return [i, nums.index(target - nums[i],i+1)]
            except:
                pass
        """