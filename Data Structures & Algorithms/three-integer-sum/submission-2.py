class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs=defaultdict(list)
        ans=[]
        
        for i in range(len(nums)):
            pairs[nums[i]]=i
        for i in range(len(nums)):
            x=nums[i]
            for j in range(i+1,len(nums)): 
                y=nums[j]
                if -(x+y) in pairs and pairs[-(x+y)] not in (i,j):
                    new=sorted([x,y,-(x+y)])
                    if new not in ans:
                        ans.append(new)
        return ans