class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor operation
        r = 0
        for n in nums:
            r ^= n
        
        return r
        
        """
        # list operation
        seen = set()
        for n in nums:
            if n in seen:
                seen.remove(n)
            else:
                seen.add(n)
        return list(seen)[0]
        """
