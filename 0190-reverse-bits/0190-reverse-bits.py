class Solution:
    def reverseBits(self, n: int) -> int:
        # res = 00000 ... 00000 32개 만큼의 0
        res = 0
        
        for i in range(32):
            # bit = n의 i번째 bit    
            # i가 n의 오른쪽에서부터 시작한다고 봤을때
            bit = (n >> i) & 1
            
            # 이때까지 구한 res는 살리고 n의 i번째 bit를
            # res의 왼쪽에서 봤을때 i번째에 심어주는 과정
            res = res | (bit << (31-i))
        
        return res