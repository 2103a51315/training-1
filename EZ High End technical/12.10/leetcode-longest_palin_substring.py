class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalin_rev(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]
        res="" 
        for i in range(len(s)):
            if len(s)==1:
                return s
            pal1=ispalin_rev(i,i)
            if len(pal1)>len(res):
               res=pal1
            pal2=ispalin_rev(i,i+1)
            if len(pal2)>len(res):
               res=pal2
        return res