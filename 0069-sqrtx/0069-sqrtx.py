class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # For x = 0 and x = 1
        if x <= 1: return x

        start = 2
        end = x
        
        # Apply Binary Search since range 1 to x is in sorted order
        while start <= end:
            mid = start + (end - start)  // 2
            
            square = mid * mid
            
            if square == x: return mid
            if square < x: start = mid + 1
            else: end = mid - 1
        
        # If the number is not a perfect square, return the value "end"
        return end