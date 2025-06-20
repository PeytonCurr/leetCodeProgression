#Bit Mask -1 Solution: TO(1) - SO(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        oneC = 0
        for i in range(32):
            if n & (1 << i):
                oneC += 1
        return oneC