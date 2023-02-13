class Solution(object):
    def generate(self, numRows):
        # My Solution
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
    
        # NeetCode https://www.youtube.com/watch?v=nPVEaB3AjUM&ab_channel=NeetCode
        res = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + [res-1] + [0]
            row = []
            for j in range(len(res-1)+1):
                row.append(temp[j]+[j+1])
            res.append(row)
        
        return res
            
                