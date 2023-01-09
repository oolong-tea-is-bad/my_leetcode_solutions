class Solution(object):
    def twoSum(self, nums, target):

        # key = num in arry / vale = index of the num
        prevMap = {}

        # i = index / n = num in array
        for i, n in enumerate(nums):        # Maybe enumerate is not absolutely needed
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
