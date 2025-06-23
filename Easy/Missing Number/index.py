#Bitwise XOR Solution: TO(n) - SO(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i,n in enumerate(nums):
            res ^= i^n
        return res