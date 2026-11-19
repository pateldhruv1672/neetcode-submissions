class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for x in nums:
            if s.get(x) is None:
                s[x] = x
            else:
                return True
        return False

            
        