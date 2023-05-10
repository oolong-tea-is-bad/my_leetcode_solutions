class Solution:
    def isHappy(self, n: int) -> bool:
        # NeetCode
        
        # 제곱하면서 발견한 새로운 숫자 저장할 세트
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            # 만약 제곱의 과정에서 1 발견하면 바로 리턴
            # 왜냐하면 1을 발견해도 계속해서 infinite loop
            if n == 1:
                return True
            
        # n이 이미 본적 있는 숫자고 1이 아니라면 n이 unhappy한거기 때문에 False
        return False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0
        
        while n:
            # n의 1의 자리 숫자
            digit = n % 10
            squaredDigit = digit ** 2
            output += squaredDigit
            # n의 1의 자리 숫자가 없어짐.
            n = n // 10
            
        return output