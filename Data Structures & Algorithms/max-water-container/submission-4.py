class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW=0
        curr=0
        l=0
        r=len(heights)-1
        while(r>=l):
            
            if heights[l]>=heights[r]:
                curr=heights[r]*(r-l)
                maxW=max(maxW,curr)
                r-=1
            elif heights[r]>heights[l]:
                curr=heights[l]*(r-l)
                maxW=max(maxW,curr)
                l+=1
        return maxW
            