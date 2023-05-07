class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        res = 0
        
        for i in range(0, len(columnTitle)):
            res += (26**i) * (ord(columnTitle[i]) - 64)
            
        return res
            