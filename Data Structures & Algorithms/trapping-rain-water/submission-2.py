class Solution:
    def trap(self, height: List[int]) -> int:
        bounds=defaultdict(list)
        seen=[]
        water=0
        for i in range(len(height)):
            for x in range(height[i]):
                bounds[x].append(i)
        for i in range(max(height)):
            for x in range(1,len(bounds[i])):
                water+=(bounds[i][x]-bounds[i][x-1]-1)
        return water