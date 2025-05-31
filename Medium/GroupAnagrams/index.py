#Sorting Solution - Time: O(m * nlogn) Space: O(m * n)
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = {}
    for s in strs:
      sortedS = ''.join(sorted(s))
      if sortedS not in res:
        res[sortedS] = []
      res[sortedS].append(s)
    return res.values()
