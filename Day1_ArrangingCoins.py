# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.

# n is a non-negative integer and fits within the range of a 32-bit signed integer.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==0:
            return 0
        ans=0
        i=1
        while ans<n:
            ans=(i*(i+1))/2
            if ans==n:
                return i
            if ans>n:
                return i-1
            i+=1
        return i
        