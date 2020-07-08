# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        if len(arr)<2:
            return []
        if max(arr)==0 and min(arr)==0 and len(arr)>2:
            return [[0,0,0]]
            
        n=len(arr)
        li=[]
        s=set()
        for i in range(n-1):
            a=set()
            for j in range(i+1,n):
                x=-(arr[i]+arr[j])
                if x in a:
                    if tuple(sorted([arr[i],x,arr[j]])) not in s:
                        li.append(sorted([arr[i],x,arr[j]]))
                        s.add(tuple(sorted([arr[i],x,arr[j]])))
                    
                else:
                    a.add(arr[j])
        return sorted(li)