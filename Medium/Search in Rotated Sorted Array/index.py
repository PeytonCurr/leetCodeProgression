#Binary Search (Two Pass) Time O(logn) - Space (1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r-l)//2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        if target > nums[len(nums) - 1]:
            newL, newR = 0, l - 1
        else:
            newL, newR = l, len(nums) - 1
        while newL <= newR:
            mid = newL + ((newR-newL)//2)
            if target > nums[mid]:
                newL = mid + 1
            elif target < nums[mid]:
                newR = mid - 1
            else:
                return mid
        return -1