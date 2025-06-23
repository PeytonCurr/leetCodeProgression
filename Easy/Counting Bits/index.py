#Bit Mask -2 Solution: TO(nlogn) - SO(1)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            while i != 0:
                i = i&i-1
                count += 1
            res.append(count)
        return res