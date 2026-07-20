class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        prod=1
        prod2=1
        for i in nums:
            if i!=0:
                prod*=i
            else:
                prod2=0
        print(prod,prod2)
        for i,x in enumerate(nums):
            print(x)
            if prod2==0 and x!=0 or nums.count(0)>1:
                out.append(prod2)
            elif x!=0:
                out.append(prod//x)
            else:
                out.append(prod)
        return out

        