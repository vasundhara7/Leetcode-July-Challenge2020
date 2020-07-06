# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        l=[]
        n=len(digits)
        for i in range(n-1,-1,-1):
            if i==n-1:
                s=1+digits[i]
            else:
                s=carry+digits[i]
            if s>9:
                s=s%10
                carry=1
            else:
                carry=0
            l.insert(0,s)
        
        if carry:
            l.insert(0,carry)
        return l