class Solution:
    def longestConsecutive(self, num: List[int]) -> int:
        x=1
        maxL=0
        l=1
        num.sort()
        for x in range(1,len(num)):
            if num[x]-1==num[x-1]:
                l+=1
            elif num[x]==num[x-1]:
                continue
            else:
                maxL=max(l,maxL)
                l=1
        maxL=max(l,maxL)
        return maxL if len(num) else 0



        
