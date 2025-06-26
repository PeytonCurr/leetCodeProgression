#Recursion Solution: TO(n^2) - SO(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)
    
#Memoization Solution: TO(n) - SO(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        res = {}
        if n <= 3:
            return n
        if n in res:
            return res[n]
        res[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return res[n]
    
#Tabulation Solution: TO(n) - SO(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        res = {1:1, 2:2,3:3}
        for i in range(4,n+1):
            res[i] = res[i-1]+res[i-2]
        return res[n]

#[Optimized Space] Tabulation Solution: TO(n) - SO(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev, curV = 0, 1, 1
        for _ in range(1,n+1):
            curV = prev + prev2
            prev2 = prev
            prev = curV
        return curV