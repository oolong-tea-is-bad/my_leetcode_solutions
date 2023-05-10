class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle의 길이 만큼의 섹션을 haystack에서 계속 검색할거임
        for i in range(len(haystack) - len(needle) + 1):
            
            # 그 섹션이 needle과 같다면
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1