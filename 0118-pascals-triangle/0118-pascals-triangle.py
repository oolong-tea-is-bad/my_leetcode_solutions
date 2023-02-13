class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """   
        res = [[1]]
        
        for i in range(numRows-1):
            nextRow = []
            for j in range(len(res[i])+1):
                if j == 0 or j == len(res[i]):
                    nextRow.append(1)
                else:
                    nextRow.append(res[i][j-1] + res[i][j])
            res.append(nextRow)
        
        return res
            
                