#Sorting Solution - Time: O(nlogn) Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        ary = []
        for n, cnt in count.items():
            ary.append([cnt,n])
        ary.sort()
        res = []
        while len(res) < k:
            res.append(ary.pop()[1])
        return res

#Bucket Sort Solution - Time: O(n) Space: O(n)
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        countA = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, cnt in count.items():
            countA[cnt].append(n)

        res = []
        for i in range(len(countA) - 1, 0 , -1):
            for n in countA[i]:
                res.append(n)
                if len(res) == k:
                    return res