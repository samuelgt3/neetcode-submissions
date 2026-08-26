class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        sCounter=defaultdict(int)
        tCounter=defaultdict(int)
        matches=0
        target=len(t)
        for i in t:
            tCounter[i]+=1
        l=0
        ans=[-1,-1]
        minL=float('infinity')
        for r in range(len(s)):

            c=s[r]
            if c in tCounter and sCounter[c]<tCounter.get(c,0):
                    matches+=1
            sCounter[c]+=1

            while (matches==target):
                length=r-l+1
                if length<minL:
                    ans=[l,r]
                    minL=length
                sCounter[s[l]]-=1
                if s[l] in tCounter and sCounter[s[l]]<tCounter.get(s[l],0):
                        matches-=1
                l+=1
        l,r=ans
        print(ans)
        return s[l:r+1] if minL<=len(s) else ""
        