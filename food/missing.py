class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res=1
        for num in nums:
            if num==res:
                res+=1
            elif num >res:
                break
        return res
        
arr=[2,3,4,1,7]
obj=Solution()
print("missing is",obj.firstMissingPositive(arr))
        
        