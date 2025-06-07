#Optimal Two Pointer Solution - Time: O(n) Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        while l < r:
            while l < r and not self.isAlphanumeric(s[l]):
               l += 1
            while r > l and not self.isAlphanumeric(s[r]):
               r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    def isAlphanumeric(self, c) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
    #My Two Pointer Solution - Time: O(n) Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        res = []
        for c in s:
            if self.isAlphanumeric(c):
                res.append(c.lower())
        j = len(res)-1
        for i,_ in enumerate(res):
            if res[i] != res[j]:
                return False
            j -= 1
        return True