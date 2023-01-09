class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
    
        if s[0] == "I":
            res += 1
        elif s[0] == "V":
            res += 5
        elif s[0] == "X":
            res += 10
        elif s[0] == "L":
            res += 50
        elif s[0] == "C":
            res += 100
        elif s[0] == "D":
            res += 500
        else:
            res += 1000

        for i in range(1, len(s)):
            if s[i] == "I":
                res += 1
            elif s[i] == "X":
                if s[i-1] == "I":
                    res += 8
                else:
                    res += 10
            elif s[i] == "C":
                if s[i-1] == "X":
                    res += 80
                else:
                    res += 100
            elif s[i] == "V":
                if s[i-1] == "I":
                    res += 3
                else:
                    res += 5
            elif s[i] == "L":
                if s[i-1] == "X":
                    res += 30
                else:
                    res += 50
            elif s[i] == "D":
                if s[i-1] == "C":
                    res += 300
                else:
                    res += 500
            else:
                if s[i-1] == "C":
                    res += 800
                else:
                    res += 1000
        
        return res