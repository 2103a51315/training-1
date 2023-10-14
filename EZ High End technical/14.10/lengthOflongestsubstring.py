class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,longestSubstring=0,0
        sw=set()
        for r in range(len(s)):
            while s[r] in sw:
                sw.remove(s[l])
                l+=1
            sw.add(s[r])
            longestSubstring=max(longestSubstring,(r-l+1))
        return longestSubstring
                    
