class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # https://www.youtube.com/watch?v=7pnhv842keE&ab_channel=NeetCode
        res, count = 0, 0
        
        # Boyer Moore Algorithm
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
            
        return res