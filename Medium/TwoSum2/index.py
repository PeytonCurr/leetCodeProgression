class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftP = 0
        rightP = len(numbers) - 1
        
        while leftP < rightP:
            if numbers[leftP] + numbers[rightP] == target:
                return [leftP + 1, rightP + 1]
            elif numbers[leftP] + numbers[rightP] > target:
                rightP -= 1
            else:
                leftP += 1
        return []