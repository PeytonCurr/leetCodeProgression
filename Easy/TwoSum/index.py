class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCheck = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numCheck:
                return [numCheck[diff], i] 
            numCheck[nums[i]] = i
        return