class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        
        digits[0] += 1
        
        if digits[0] == 10:
            for i in range(0, len(digits)-1):
                if digits[i] == 10:
                    digits[i] -= 10
                    digits[i+1] += 1
        
        if digits[-1] == 10:
            digits[-1] = 0
            digits.append(1)
        
        digits.reverse()
        return digits