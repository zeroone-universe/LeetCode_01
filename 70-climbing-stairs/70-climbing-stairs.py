class Solution:
    def climbStairs(self, n: int) -> int:
        def factorial(n):
            ret=1
            for i in range(1,n+1):
                ret*=i
            return ret
        
        a,b=divmod(n,2)
        ans=0
        for i in range(a+1):
            j=n-2*i
            ans+=factorial(j+i)/(factorial(j)*factorial(i))
        return int(ans)
            