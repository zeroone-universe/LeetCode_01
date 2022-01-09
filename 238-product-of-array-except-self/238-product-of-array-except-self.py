class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toright=[1,1]
        toleft=[]
        ans=[]
        
        i,j=1,1
        for num in nums:
            i=i*num
            toright.append(i)
            
        for num in nums[::-1]:
            j=j*num
            toleft.append(j)
            
        toleft=toleft[::-1]+[1,1]
        for i in range(len(toleft)):
            ans.append(toleft[i]*toright[i])
        
        return ans[1:len(ans)-1]