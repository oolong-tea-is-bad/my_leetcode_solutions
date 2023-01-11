class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 : 1
        # 2 : 2
        # 3 : 3
        # 4 : 5
        # 5 : 8
        
        # fibonacci
        
        one, two = 1, 1
        
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        
        return one
        