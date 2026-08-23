class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL=0
        l=0
        seen=[]
        pos={}
        for r in range(len(s)):
            if s[r] in seen:
                maxL=max(maxL,len(seen))
                seen=seen[pos[s[r]]-l+1:]
                l=pos[s[r]]+1
            pos[s[r]]=r
            seen.append(s[r])
        return max(maxL,len(seen))