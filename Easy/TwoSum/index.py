#Brute Force - Nested Loop Solution - Time: O(n^2) Space: O(1)
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i, _ in enumerate(nums):
      for j, _ in enumerate(nums):
        if nums[i] + nums[j] == target:
          return [i,j]
    return []

#One Pass - Hashmap Solution - Time: O(n) Space: O(n)
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i