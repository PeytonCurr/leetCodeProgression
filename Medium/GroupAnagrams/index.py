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
  

#Hashmap Solution - Time: O(m * n) Space: O(m * n)
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord('a')] += 1
      res[tuple(count)].append(s)
    return res.values()