class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct=collections.Counter(nums)
        a=ct.most_common(k)
        ls=[]
        for i in a:
            ls.append(i[0])
        return ls