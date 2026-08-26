class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        l=0
        for r in range(k):
            while q and nums[r]>q[-1]:
                q.pop()
            q.append(nums[r])
        ans=[q[0]]
        for r in range(k,len(nums)):
            while q and nums[r]>q[-1]:
                q.pop()
            q.append(nums[r])
            if nums[l]==q[0]:
                q.popleft()
            l+=1
            ans.append(q[0])
        return ans