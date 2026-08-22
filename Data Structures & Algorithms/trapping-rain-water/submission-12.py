class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        maxL=[0]
        maxR=[0]
        diff=[]
        l=0
        r=0
        for i in range(1,len(height)):
            l=max(l,height[i-1])
            maxL.append(l)
        for i in range(-2,-len(height)-1,-1):
            r=max(r,height[i+1])
            maxR.append(r)
        for i in range(len(height)):
            l=maxL[i]
            r=maxR[-(i+1)]
            d=min(l,r)
            diff.append(d)
        for i in range(len(height)):
            dif=max(diff[i]-height[i],0)
            water+=dif
        return water