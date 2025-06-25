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


#[Optimized Space] Tabulation Solution: TO(n) - SO(n)