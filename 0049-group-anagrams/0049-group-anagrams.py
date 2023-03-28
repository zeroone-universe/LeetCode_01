class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        output = []
        
        if len(strs)<=1:
            return [strs]
        
        dd = collections.defaultdict(list)
        
        for str in strs:
            dd["".join(sorted(list(str)))].append(str)


        for item in dd.items():
            output.append(item[1])
            
        return output

        
        