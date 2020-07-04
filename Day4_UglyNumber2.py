# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        dp=[1]*n
        i2=i3=i5=0
        for i in range(1,n):
            nm2=dp[i2]*2
            nm3=dp[i3]*3
            nm5=dp[i5]*5
            dp[i]=min(nm2,nm3,nm5)
            if nm2 == min(nm2,nm3,nm5):
                i2+=1
            if nm3==min(nm2,nm3,nm5):
                i3+=1
            if nm5==min(nm2,nm3,nm5):
                i5+=1
        return dp[n-1]
        