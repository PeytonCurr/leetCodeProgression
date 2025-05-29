#Brute Force - Nested Loop Solution
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, _ in enumerate(nums):
      for j, _ in enumerate(nums):
        if nums[i] + nums[j] == target:
          return [i,j]
    return []

#One Pass - Hashmap Solution
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i