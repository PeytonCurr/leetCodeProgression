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

#Hashmap Solution - Time: O() Space: O()
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      