#Optimal Sliding Window Solution - Time: O(n) Space: O(m)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res = 0, 0
        inWindow = set()
        for r in range(len(s)):
            while s[r] in inWindow:
                inWindow.remove(s[l])
                l += 1
            inWindow.add(s[r])
            res = max(res, len(inWindow))
        return res