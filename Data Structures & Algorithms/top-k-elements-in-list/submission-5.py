class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        count=Counter(nums)
        print(count)
        while(len(ans)<k):
            max_k=max(count, key=count.get)
            ans.append(max_k)
            del(count[max_k])
        return ans