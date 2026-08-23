class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=0
        found=[]
        l1=sorted(list(s1))
        if s1 in s2:
            return True
        while(l<=len(s2)-len(s1)):
            if s2[l] in s1:
                for r in range(l,l+len(s1)):
                    if s2[r] in s1:
                        found.append(s2[r])
                    else:
                        break
                
                if sorted(found)==l1:
                    return True
                found.clear()
            l+=1
        return False

        
