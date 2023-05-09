class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numDic = {nums[0]:1}
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] not in numDic:
                numDic[nums[i]] = 1
                k += 1
                
                nums[k-1] = nums[i]

        return k
        
            