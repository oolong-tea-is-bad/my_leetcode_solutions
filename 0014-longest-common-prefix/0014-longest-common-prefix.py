class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        
        res = ""
        strs.sort(key=len)

        for i in range(len(strs[0])):
            res += strs[0][i]
            for j in range(len(strs)-1):
                if strs[j][i] != strs[j+1][i]:
                    res = res[0:i]
                    return res
            
        return res