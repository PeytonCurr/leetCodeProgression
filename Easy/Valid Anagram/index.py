# My Sorting Solution(No Help) - Time: O(nlogn + mlogm) / Space: O(1) or O(n + m)
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
       return False
    sortedS = sorted(s)
    sortedT = sorted(t)
    for i in range(len(sortedS)):
       if sortedS[i] != sortedT[i]:
          return False
    return True

# Optimal Sorting Solution - Time: O(nlogn + mlogm) / Space: O(1) or O(n + m)
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
       return False
    return sorted(s) == sorted(t)

# Hashmap Solution - Time: O(n + m) / Space: O(1) Only Constant cause 26 Max Characters (Alphabet)
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT