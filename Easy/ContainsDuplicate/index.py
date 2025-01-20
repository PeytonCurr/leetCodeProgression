# Brute Force Solution - Time: O(n^2) / Space: O(1)
def hasDuplicate(self, nums: List[int]) -> bool:
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if nums[i] == nums[j]:
        return True
  return False

# Sorting Solution - Time: O(nlogn) / Space: O(1)
def hasDuplicate(self, nums: List[int]) -> bool:
  nums.sort()
  for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
      return True
  return False

# Hashmap solution - Time: O(n) / Space: O(n)
class Solution:
def containsDuplicate(self, nums: List[int]) -> bool:
  nums.sort()
  n = len(nums)
  for i in range(1, n):
    if(nums[i] == nums[i - 1]):
      return True
  return False